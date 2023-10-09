from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template("hatespeechdetection.html")
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        
        text = request.form['input']
        with  open('model.pkl', 'rb') as file:
            model = pickle.load(file)
        text = text.lower()
        text = re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
        prediction = model.predict([text])
        if prediction == 0:
            output = "Not Hate Speech"
        else:
            output = "Hate Speech"
            
        return render_template("hatespeechdetection.html", output=output)
        
if __name__ == "__main__":
    app.run(debug=True)
