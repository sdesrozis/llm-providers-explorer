from together import Together
from dotenv import load_dotenv

load_dotenv()

client = Together()

free_models = [model for model in client.models.list() if model.id.endswith('-Free')]

for model in free_models:
    print(model.id)

response = client.chat.completions.create(
    model=free_models[1].id,
    messages=[
        {
            "role": "user", 
            "content": "What are some fun things to do in New York?"
        }
    ],
    stream=True,
)

for chunk in response:
    if chunk.choices:
        content = chunk.choices[0].delta.content
        print(content, end="", flush=True)
print()
