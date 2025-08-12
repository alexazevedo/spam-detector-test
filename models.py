from pydantic import BaseModel


class ClassificationResult(BaseModel):
    is_spam: bool
    reason: str
