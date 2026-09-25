from dataclasses import dataclass
from typing import Protocol, Any


class ModelProvider(Protocol):
    def generate(self, prompt: str) -> str: ...


@dataclass
class Evaluation:
    prompt: str
    response: str
    passed: bool
    score: float


@dataclass
class TrainingCandidate:
    schema_version: str
    task: str
    intent: str
    strategy: str
    validated_answer: str
    evidence_refs: list[dict[str, str]]
    scores: dict[str, float | None]


def evaluate_candidate(candidate: TrainingCandidate) -> Evaluation:
    """Validate a candidate without pretending that validation is model training."""
    answer = candidate.validated_answer.strip()
    passed = bool(answer) and candidate.schema_version == "trainer-candidate-v1"
    score = 1.0 if passed else 0.0
    return Evaluation(candidate.task, answer, passed, score)


class MockProvider:
    def generate(self, prompt: str) -> str:
        return f"Mock response: {prompt}"


def evaluate(provider: ModelProvider, prompt: str) -> Evaluation:
    response = provider.generate(prompt)
    passed = bool(response.strip())
    score = 1.0 if passed else 0.0
    return Evaluation(prompt, response, passed, score)


def normalize_candidate(payload: dict[str, Any]) -> TrainingCandidate:
    """Convert the Web contract into the Trainer's internal evaluation shape."""
    return TrainingCandidate(
        schema_version=str(payload.get("schema_version", "")),
        task=str(payload.get("task", ""))[:1000],
        intent=str(payload.get("intent", "general"))[:120],
        strategy=str(payload.get("strategy", "general-reasoning"))[:240],
        validated_answer=str(payload.get("validated_answer", ""))[:6000],
        evidence_refs=list(payload.get("evidence_refs", []))[:8],
        scores=dict(payload.get("scores", {}))
    )


@dataclass
class Lesson:
    schema_version: str
    task: str
    intent: str
    strategy: str
    validated_answer: str
    evidence_refs: list[dict[str, str]]
    confidence: float
    lesson_key: str


def build_lesson(candidate: TrainingCandidate, evaluation: Evaluation) -> Lesson | None:
    """Create a bounded reusable lesson only from a passed candidate."""
    if not evaluation.passed:
        return None
    answer = candidate.validated_answer.strip()
    key = f"{candidate.intent}:{candidate.strategy}:{candidate.task.strip().lower()[:240]}"
    scores = [v for v in candidate.scores.values() if isinstance(v, (int, float))]
    confidence = min(1.0, max([evaluation.score, *[float(v) for v in scores]] or [0.0]))
    return Lesson(
        schema_version="bitey-lesson-v1",
        task=candidate.task,
        intent=candidate.intent,
        strategy=candidate.strategy,
        validated_answer=answer,
        evidence_refs=candidate.evidence_refs,
        confidence=confidence,
        lesson_key=key,
    )


def deduplicate_lessons(lessons: list[Lesson]) -> list[Lesson]:
    """Keep the highest-confidence lesson for each bounded semantic key."""
    best: dict[str, Lesson] = {}
    for lesson in lessons:
        current = best.get(lesson.lesson_key)
        if current is None or lesson.confidence > current.confidence:
            best[lesson.lesson_key] = lesson
    return list(best.values())
