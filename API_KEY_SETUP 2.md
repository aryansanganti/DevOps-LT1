# Groq API Key Setup

Create a Groq API key in the [Groq Console](https://console.groq.com/keys).
Set the key and model in your shell:

```bash
export GROQ_API_KEY=your_groq_api_key_here
export GROQ_MODEL=qwen/qwen3.8-27b
```

You can instead copy `.env.example` to `.env` and set those values there.
Keep `.env` private and never commit API keys.

Revoke any key that has been pasted into a public document or chat, then use a
new key.
