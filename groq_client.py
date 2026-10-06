"""Shared Groq API configuration and text generation."""

import os
from typing import Optional

from groq import Groq


DEFAULT_GROQ_MODEL = "qwen/qwen3.8-27b"


def get_groq_model() -> str:
    """Return the configured Groq model, or the project default."""
    model = os.getenv("GROQ_MODEL", DEFAULT_GROQ_MODEL).strip()
    if not model:
        raise ValueError("GROQ_MODEL must not be empty.")
    return model


def create_groq_client(api_key: Optional[str] = None) -> Groq:
    """Create a Groq client using an explicit key or GROQ_API_KEY."""
    key = api_key or os.getenv("GROQ_API_KEY")
    if not key or not key.strip():
        raise ValueError("GROQ_API_KEY is required to use Groq.")
    return Groq(api_key=key.strip())


def generate_text(
    client: Groq,
    prompt: str,
    system_instruction: Optional[str] = None,
    model: Optional[str] = None,
) -> str:
    """Generate text through Groq chat completions."""
    messages = []
    if system_instruction:
        messages.append({"role": "system", "content": system_instruction})
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=model or get_groq_model(),
        messages=messages,
    )
    if not response.choices:
        raise RuntimeError("Groq returned no completion choices.")
    content = response.choices[0].message.content
    if content is None:
        raise RuntimeError("Groq returned an empty response.")
    return content
