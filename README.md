# Email Importance API

A simple Flask API that classifies email subject lines by importance using a trained ML model.

## Features
- Classifies into: High, Medium, or Low
- REST API for integration with extensions or other apps

## Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the API
```bash
python app.py
```

The server will start at `http://localhost:5000`.

### 3. Example POST request
```json
POST /predict
Content-Type: application/json

{
  "text": "project update"
}
```

Response:
```json
{
  "importance": "Medium"
}
```

## Deploy to Render

1. Push this folder to a GitHub repo.
2. Go to [https://render.com](https://render.com) and create a new Web Service.
3. Link your repo and use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
4. Render will provide a public API URL.