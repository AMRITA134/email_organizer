from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("email_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    
    transformed_text = vectorizer.transform([text])
    print("Input vector:", transformed_text)

    prediction = model.predict(transformed_text)[0]
    return jsonify({'importance': prediction})
