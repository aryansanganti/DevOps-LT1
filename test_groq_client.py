from unittest.mock import Mock, patch

import pytest

from groq_client import (
    DEFAULT_GROQ_MODEL,
    create_groq_client,
    generate_text,
    get_groq_model,
)


def test_model_uses_configured_value(monkeypatch):
    monkeypatch.setenv("GROQ_MODEL", "qwen/custom-model")

    assert get_groq_model() == "qwen/custom-model"


def test_model_defaults_to_configured_project_model(monkeypatch):
    monkeypatch.delenv("GROQ_MODEL", raising=False)

    assert get_groq_model() == DEFAULT_GROQ_MODEL


def test_model_rejects_empty_config(monkeypatch):
    monkeypatch.setenv("GROQ_MODEL", " ")

    with pytest.raises(ValueError, match="GROQ_MODEL"):
        get_groq_model()


@patch("groq_client.Groq")
def test_client_reads_groq_api_key_from_environment(groq_constructor, monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "test-groq-key")

    create_groq_client()

    groq_constructor.assert_called_once_with(api_key="test-groq-key")


def test_client_requires_api_key(monkeypatch):
    monkeypatch.delenv("GROQ_API_KEY", raising=False)

    with pytest.raises(ValueError, match="GROQ_API_KEY"):
        create_groq_client()


def test_generate_text_sends_chat_completion_request():
    client = Mock()
    client.chat.completions.create.return_value = Mock(
        choices=[Mock(message=Mock(content="AI result"))]
    )

    result = generate_text(
        client,
        "Analyze this repository",
        system_instruction="Respond as JSON",
        model="qwen/custom-model",
    )

    assert result == "AI result"
    client.chat.completions.create.assert_called_once_with(
        model="qwen/custom-model",
        messages=[
            {"role": "system", "content": "Respond as JSON"},
            {"role": "user", "content": "Analyze this repository"},
        ],
    )


def test_generate_text_uses_model_from_environment(monkeypatch):
    monkeypatch.setenv("GROQ_MODEL", "qwen/environment-model")
    client = Mock()
    client.chat.completions.create.return_value = Mock(
        choices=[Mock(message=Mock(content="AI result"))]
    )

    generate_text(client, "prompt")

    client.chat.completions.create.assert_called_once_with(
        model="qwen/environment-model",
        messages=[{"role": "user", "content": "prompt"}],
    )


def test_generate_text_rejects_empty_response():
    client = Mock()
    client.chat.completions.create.return_value = Mock(
        choices=[Mock(message=Mock(content=None))]
    )

    with pytest.raises(RuntimeError, match="empty response"):
        generate_text(client, "prompt")


def test_generate_text_rejects_missing_choices():
    client = Mock()
    client.chat.completions.create.return_value = Mock(choices=[])

    with pytest.raises(RuntimeError, match="no completion choices"):
        generate_text(client, "prompt")
