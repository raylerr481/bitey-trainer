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
