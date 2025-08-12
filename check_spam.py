import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

model = "gpt-4o-mini"


def check_spam(email: str) -> str | None:
    prompt = f"""
    Determine if the email is spam.

    Return a valid JSON object with the format:
    {{
        is_spam: is the email spam? // bool
        reason: think step by step, why is it spam or not spam? // str
    }}

    Email: {email}"""

    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,
        max_tokens=100,
        # response_format={"type": "json_object"},
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    email = "hi how r u bro i have million dollar deal just sign here"
    res = check_spam(email)
    if res:
        print(json.dumps(json.loads(res), indent=2))
