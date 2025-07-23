from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

for model in client.models.list().data:
    print(model.id)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="deepseek-r1-distill-llama-70b",
    stream=True,
)

for chunk in response:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
print()

