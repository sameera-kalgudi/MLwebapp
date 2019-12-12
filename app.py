import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.image as mpimg 
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import json
import pickle
from keras.models import model_from_json


ALLOWED_EXTENSIONS = set(['csv'])
UPLOAD_FOLDER = 'C:/Users/Samee/Desktop/Heroku-Demo-master/master/ML-group-project/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app_root = os.path.dirname(os.path.abspath(__file__))
new_model = pickle.load(open("C:/Users/Samee/Desktop/Heroku-Demo-master/master/ML-group-project/model.pkl",'rb'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		#for file in request.form['file']:
		file = request.files['file']
		file.save(os.path.join(UPLOAD_FOLDER, "img.csv"))
		p = pd.read_csv("C:/Users/Samee/Desktop/Heroku-Demo-master/master/ML-group-project/uploads/img.csv")
		#file = pd.read_csv('C:/Users/Samee/Desktop/Heroku-Demo-master/master/ML-group-project/testing.csv') 
			#filename = secure_filename(file.filename)
			#sfname = 'uploads/'+str(secure_filename(file.filename))
		prediction = new_model.predict(p)
		#o = new_model.evaluate(p)
		output = prediction.argmax()
	return render_template('index.html', prediction_text='Predicted image is : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)