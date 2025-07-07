from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load("model.pkl")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/project')
def project():
    return render_template("project.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        brand = int(request.form['brand_name'])
        owner = int(request.form['owner'])
        age = float(request.form['age'])
        power = float(request.form['power'])
        kms_driven = float(request.form['kms_driven'])

        input_features = np.array([[brand, owner, age, power, kms_driven]])
        prediction = model.predict(input_features)[0]

        return render_template("project.html", prediction=round(prediction, 2))

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/history')
def history():
    return render_template("history.html")

if __name__ == '__main__':
    app.run(debug=True)
