import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [
    "urgent: server is down", "please review this asap", 
    "meeting schedule", "project update", 
    "weekly newsletter", "social event"
]
labels = ["High", "High", "Medium", "Medium", "Low", "Low"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
model = LogisticRegression()
model.fit(X, labels)

joblib.dump(model, "email_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")