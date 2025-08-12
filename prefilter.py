import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def build_pipeline() -> Pipeline:
    return Pipeline(
        [
            ("tfidf", TfidfVectorizer(
                ngram_range=(1, 2),
                min_df=2,
                max_df=0.95
            )),
            ("clf", LogisticRegression(max_iter=300, class_weight="balanced")),
        ]
    )


def train_prefilter(texts: list[str], labels: list[int]) -> Pipeline:
    pipe = build_pipeline()
    pipe.fit(texts, labels)
    return pipe


def save_prefilter(pipe: Pipeline, path: str) -> None:
    joblib.dump(pipe, path)


def load_prefilter(path: str) -> Pipeline:
    return joblib.load(path)


def predict_spam_prob(pipe: Pipeline, texts: list[str]) -> list[float]:
    return pipe.predict_proba(texts)[:, 1].tolist()
