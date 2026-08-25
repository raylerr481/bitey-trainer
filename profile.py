from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class HumanProfile:
    name: str
    location: str
    languages: dict
    technical_skills: List[str] = field(default_factory=list)
    office_skills: List[str] = field(default_factory=list)
    writing_skills: List[str] = field(default_factory=list)
    education: List[str] = field(default_factory=list)
    ai_collaboration: bool = True


PRIMARY_PROFILE = HumanProfile(
    name="Rayler",
    location="Brazil",
    languages={"Spanish": "fluent", "Portuguese": "basic", "English": "intermediate"},
    technical_skills=["IT", "Python", "PHP", "JavaScript", "networks", "databases", "cloud", "AI", "APIs"],
    office_skills=["Microsoft Excel", "Microsoft Word", "data entry", "document management", "QA"],
    writing_skills=["fast typing", "technical writing", "content review", "structured feedback"],
    education=["Education", "Computer Science"],
)
