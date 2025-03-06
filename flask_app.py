from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

FASTAPI_URL = "http://127.0.0.1:8000/predict/"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict/", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        print(f"📤 Sending data to FastAPI: {data}")

        response = requests.post(FASTAPI_URL, json=data)
        print(f"📥 Received response from FastAPI: {response.status_code}, {response.text}")

        response.raise_for_status()  # Raise error for non-200 responses
        return jsonify(response.json())  # Forward response to UI
    except requests.exceptions.RequestException as e:
        print("❌ Request Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

