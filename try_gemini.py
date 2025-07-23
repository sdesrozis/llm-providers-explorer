import os
from google import genai
from dotenv import load_dotenv

load_dotenv()


client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

for model in client.models.list():
    print(model.name)

response = client.models.generate_content_stream(
    model="gemini-2.0-flash", 
    contents="Explain how AI works",
)

for chunk in response:
    print(chunk.text, end="")
print()
