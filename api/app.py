from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "Smart Factory Predictive Maintenance API is running"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json
    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    return jsonify({"machine_failure": int(prediction)})

if __name__ == "__main__":
    app.run(port=5000)