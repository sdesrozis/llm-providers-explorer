# 🔍 Free LLM Model Explorer

This is a lightweight Python project that helps you **explore and test free or publicly accessible LLMs** (when available) across multiple providers:

- [Together.ai](https://www.together.ai/)
- [Google Gemini](https://ai.google.com/gemini/)
- [OpenRouter](https://openrouter.ai/)
- [Groq](https://groq.com/)
- [Mistral](https://mistral.ai/)

Each script lets you quickly test model access and behavior using your API keys.

## 🛠️ Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file with your `API` keys:

```bash
# MISTRAL_API_KEY=...
# OPENROUTER_API_KEY=...
# TOGETHER_API_KEY=...
# GEMINI_API_KEY=...
# GROQ_API_KEY=...
```

Run any of the test scripts directly with Python:

```bash
python try_openrouter.py
python try_groq.py
```