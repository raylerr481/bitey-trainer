from dataclasses import dataclass
from typing import Iterable
from trainer import Lesson


@dataclass(frozen=True)
class LessonMatch:
    lesson: Lesson
    relevance: float


def _tokens(value: str) -> set[str]:
    return {token for token in value.lower().split() if len(token) > 2}


def lesson_relevance(task: str, intent: str, lesson: Lesson) -> float:
    query = _tokens(f"{task} {intent}")
    candidate = _tokens(f"{lesson.task} {lesson.intent} {lesson.strategy}")
    if not query or not candidate:
        return 0.0
    overlap = len(query & candidate) / len(query | candidate)
    return min(1.0, overlap * 0.75 + lesson.confidence * 0.25)


def retrieve_lessons(task: str, intent: str, lessons: Iterable[Lesson], limit: int = 5, min_relevance: float = 0.35) -> list[LessonMatch]:
    """Rank prior lessons as optional context; current evidence remains authoritative."""
    matches = [LessonMatch(lesson, lesson_relevance(task, intent, lesson)) for lesson in lessons]
    matches = [match for match in matches if match.relevance >= min_relevance]
    matches.sort(key=lambda match: match.relevance, reverse=True)
    return matches[:max(0, limit)]


def build_learning_context(matches: Iterable[LessonMatch]) -> list[dict[str, object]]:
    """Expose bounded prior-learning hints without treating them as current evidence."""
    return [
        {
            "lesson_key": match.lesson.lesson_key,
            "strategy": match.lesson.strategy,
            "confidence": round(match.lesson.confidence, 4),
            "validated_answer": match.lesson.validated_answer[:2000],
            "evidence_refs": match.lesson.evidence_refs[:8],
            "authority": "prior-learning-context",
        }
        for match in matches
    ]
