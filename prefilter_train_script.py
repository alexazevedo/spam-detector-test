import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split

from prefilter import predict_spam_prob, save_prefilter, train_prefilter
from utils import prepare

IN_PATH = "samples.csv"      # columns: body, label (0=ham, 1=spam)
OUT_PATH = "prefilter.joblib"


def load_dataset(path: str):
    df = pd.read_csv(path)
    df = df.dropna(subset=["body", "label"])
    texts = [prepare(b) for b in df["body"]]
    labels = df["label"].astype(int).tolist()
    return texts, labels


if __name__ == "__main__":
    texts, labels = load_dataset(IN_PATH)
    X_tr, X_val, y_tr, y_val = train_test_split(
        texts, labels, test_size=0.2, random_state=42, stratify=labels
    )

    pipe = train_prefilter(X_tr, y_tr)

    print("Quick eval:")
    p = predict_spam_prob(pipe, X_val)
    y_pred = (np.array(p) >= 0.5).astype(int)
    print(classification_report(y_val, y_pred, digits=3))
    print("ROC-AUC:", roc_auc_score(y_val, p))

    save_prefilter(pipe, OUT_PATH)
    print(f"Saved: {OUT_PATH}")
