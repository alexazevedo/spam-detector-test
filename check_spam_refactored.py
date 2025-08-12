from utils import prepare
from prefilter import predict_spam_prob, load_prefilter
from models import ClassificationResult
from llm import create_client, llm_classify


client = create_client()


def get_pipeline():
    return load_prefilter("prefilter.joblib")


def check_spam(email_message: str) -> str | None:
    # thresholds for low confidence
    LOW_T = 0.3
    prepared_email_message = prepare(email_message)
    pipe = load_prefilter("prefilter.joblib")
    span_prob = predict_spam_prob(pipe, [prepared_email_message])[0]

    print(f"Spam probability: {span_prob}")

    if span_prob <= LOW_T:
        return ClassificationResult(
            is_spam=False,
            reason="Low spam probability by prefilter (skipping LLM check)",
        )

    # send to LLM
    result: ClassificationResult | None = llm_classify(client, email_message)
    if result is None:
        raise Exception("Error classifying email message using LLM")

    return result.model_dump_json()


if __name__ == "__main__":
    email = "hi how r u bro i have million dollar deal just sign here"
    
    result_json = check_spam(email)
    if result_json:
        print(result_json)
