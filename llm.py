import os

from openai import OpenAI

from models import ClassificationResult


def create_client() -> OpenAI:
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def llm_classify(
    client: OpenAI, email_text: str
) -> ClassificationResult | None:
    SYSTEM_PROMPT = """You are a strict email spam classifier.
    Return ONLY a JSON object with keys: is_spam (boolean), reason (string).
    The reason must be one concise sentence."""

    try:
        response = client.responses.parse(
            model="gpt-4o-mini",
            instructions=SYSTEM_PROMPT,
            input=f"Email:\n{email_text}",
            text_format=ClassificationResult,
            temperature=0.1,
            max_output_tokens=64,
        )        
        if hasattr(response, 'output_parsed') and response.output_parsed:
            return ClassificationResult.model_validate(response.output_parsed)
        else:
            return None
    except Exception as e:
        print(f"Error trying to classify email message using LLM: {e}")
        return None
