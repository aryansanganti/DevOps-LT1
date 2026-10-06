# Groq API Key Setup

The application uses Groq for AI-powered analysis. Create a Groq API key in the [Groq Console](https://console.groq.com/keys),
then set it in your environment or local `.env` file.

```bash
export GROQ_API_KEY=your_groq_api_key_here
export GROQ_MODEL=qwen/qwen3.8-27b
```

Alternatively, copy `.env.example` to `.env` and set `GROQ_API_KEY` and
`GROQ_MODEL` there. Keep `.env` private and never commit API keys.

Run the containerizer with:

```bash
uv run python repo_containerizer.py containerize https://github.com/owner/repo
```

If an API key was pasted into a public document or chat, revoke it and create a
replacement before using the application.
