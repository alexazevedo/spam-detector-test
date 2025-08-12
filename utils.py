import re
from bs4 import BeautifulSoup


def to_text(html_or_text: str) -> str:
    txt = BeautifulSoup(html_or_text, "html.parser").get_text(" ", strip=True)
    txt = re.sub(r"\s+", " ", txt).strip()
    return txt


def clip(text: str, max_chars: int) -> str:
    return text[:max_chars]


def prepare(email_body: str) -> str:
    max_chars = 15000  # truncate email if too long
    text = f"{to_text(email_body)}"
    return clip(text, max_chars)
