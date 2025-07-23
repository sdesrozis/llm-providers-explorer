import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

free_models = [model for model in client.models.list() if model.id.endswith(':free')]

for model in free_models:
    print(model.id)

response = client.chat.completions.create(
    model=free_models[0].id,
    messages=[
        {
        "role": "user",
        "content": "What is the meaning of life?"
        }
    ],
    stream=True,
)

for chunk in response:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
print()
