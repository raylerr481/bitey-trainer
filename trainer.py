from dataclasses import dataclass
from typing import Protocol


class ModelProvider(Protocol):
    def generate(self, prompt: str) -> str: ...


@dataclass
class Evaluation:
    prompt: str
    response: str
    passed: bool
    score: float


class MockProvider:
    def generate(self, prompt: str) -> str:
        return f"Mock response: {prompt}"


def evaluate(provider: ModelProvider, prompt: str) -> Evaluation:
    response = provider.generate(prompt)
    passed = bool(response.strip())
    score = 1.0 if passed else 0.0
    return Evaluation(prompt, response, passed, score)
