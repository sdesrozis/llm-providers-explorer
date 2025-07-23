import os
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()

client = Mistral(api_key=os.environ['MISTRAL_API_KEY'])

free_models = [model for model in client.models.list().data if model.id.startswith('open')]

for model in free_models:
    print(model.id)

response = client.chat.stream(
    model=free_models[0].id,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ],
    stream=True,
)

for chunk in response:
    content = chunk.data.choices[0].delta.content
    if content:
        print(content, end="")
print()
