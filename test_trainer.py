from trainer import MockProvider, evaluate


def test_smoke_evaluation():
    result = evaluate(MockProvider(), "Explain what Bitey Trainer does.")
    assert result.passed is True
    assert result.score == 1.0
    assert "Bitey Trainer" in result.response
