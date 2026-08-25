from dataclasses import dataclass
from profile import HumanProfile, PRIMARY_PROFILE


@dataclass(frozen=True)
class Opportunity:
    title: str
    mode: str  # BITEY, HUMAN, or HYBRID
    skills: list[str]
    languages: dict
    human_required: bool = False
    agent_allowed: bool = False


def score_opportunity(opportunity: Opportunity, profile: HumanProfile = PRIMARY_PROFILE) -> tuple[float, list[str]]:
    score = 0.0
    reasons = []
    required = {s.lower() for s in opportunity.skills}
    human_skills = {s.lower() for s in profile.technical_skills + profile.office_skills + profile.writing_skills}
    matches = required & human_skills
    if required:
        score += 55 * len(matches) / len(required)
        if matches:
            reasons.append(f"matching skills: {', '.join(sorted(matches))}")

    for language, level in opportunity.languages.items():
        actual = profile.languages.get(language)
        if actual == level:
            score += 20
            reasons.append(f"language match: {language} ({level})")
        elif actual:
            score += 8
            reasons.append(f"partial language match: {language} ({actual} vs {level})")

    if opportunity.mode == "BITEY" and opportunity.agent_allowed:
        score += 15
        reasons.append("agent execution permitted")
    elif opportunity.mode == "HUMAN" and opportunity.human_required:
        score += 10
        reasons.append("human-in-the-loop opportunity")
    elif opportunity.mode == "HYBRID":
        score += 12
        reasons.append("hybrid AI + human workflow")

    return min(score, 100.0), reasons
