
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("fake_insta_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [
            int(request.form['profile_pic']),
            float(request.form['nums_length_username']),
            int(request.form['fullname_words']),
            float(request.form['nums_length_fullname']),
            int(request.form['name_equals_username']),
          
            int(request.form['external_url']),
            int(request.form['private']),
            int(request.form['posts']),
            int(request.form['followers']),
            int(request.form['follows']),
        ]
        prediction = model.predict([data])[0]
        result = "🚨 Fake Instagram Profile" if prediction == 1 else "✅ Real Instagram Profile"
        return render_template("index.html", prediction=result)
    except Exception as e:
        return render_template("index.html", prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
