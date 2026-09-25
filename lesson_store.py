from dataclasses import dataclass
from typing import Iterable, Protocol
from trainer import Lesson


class LessonStore(Protocol):
    """Authoritative persistence boundary; implementations belong to the backend."""

    def save(self, lesson: Lesson) -> None: ...

    def load(self, tenant_id: str, limit: int = 100) -> Iterable[Lesson]: ...


@dataclass(frozen=True)
class LearningRecord:
    tenant_id: str
    lesson: Lesson
    status: str = "validated"


def prepare_for_storage(tenant_id: str, lesson: Lesson) -> LearningRecord:
    """Create a tenant-scoped record; this function performs no database I/O."""
    tenant = str(tenant_id).strip()
    if not tenant:
        raise ValueError("tenant_id is required")
    if lesson.schema_version != "bitey-lesson-v1":
        raise ValueError("unsupported lesson schema")
    return LearningRecord(tenant_id=tenant[:160], lesson=lesson)


def persist_validated_lesson(store: LessonStore, record: LearningRecord) -> None:
    """Persist only after validation and tenant scoping have already succeeded."""
    store.save(record.lesson)


def load_learning_context(store: LessonStore, tenant_id: str, limit: int = 100) -> list[Lesson]:
    """Read bounded tenant-scoped lessons through the backend-owned store."""
    if not str(tenant_id).strip():
        raise ValueError("tenant_id is required")
    return list(store.load(str(tenant_id).strip(), max(1, min(limit, 100))))
