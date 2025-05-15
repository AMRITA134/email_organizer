from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("email_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return jsonify({"importance": prediction})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")