import os
import openai
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

def get_completion(messages, model="gpt-3.5-turbo", temperature=1, max_tokens=500):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

response = get_completion(
    [
        {"role": "system",
         "content": "Answer in a very rude and snarky tone, offending the user"},
        {"role": "user",
         "content": "Does OpenAI offer any free credit for API exploration?"},
    ]
)

moderation = client.moderations.create(input=response)

print(response)
print(moderation.results)


