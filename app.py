from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load('email_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def home():
    return "📬 Email Importance Classifier is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']

    # Transform the input text
    transformed_text = vectorizer.transform([text])

    # Debug: print input vector (optional)
    print("Input vector:", transformed_text)

    # Predict
    prediction = model.predict(transformed_text)[0]

    return jsonify({'importance': prediction})

if __name__ == '__main__':
    app.run(debug=True)
