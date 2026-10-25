from openai import OpenAI
import os
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="Explain the importance of fast language models",
    model="qwen/qwen3.8-27b",
    stream=True,
    max_output_tokens=300,
)
for event in response:
    if event.type == "response.output_text.delta":
        print(event.delta, end="")