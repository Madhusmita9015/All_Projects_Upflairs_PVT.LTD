from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("rain_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [
            float(request.form["actual"]),
            float(request.form["normal"]),
            float(request.form["deviation"])
        ]
        prediction = model.predict([data])[0]
        result = "🌧️ Rain Expected Tomorrow" if prediction == 1 else "☀️ No Rain Tomorrow"
        return render_template("index.html", prediction=result)
    except Exception as e:
        return render_template("index.html", prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
