import numpy as np
import tensorflow as tf
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import json
import pickle
from keras.models import model_from_json


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
tf.keras.models.load_model("C:/Users/Samee/Desktop/Heroku-Demo-master/master/ML-group-project/mnist_simple_cnn.h5")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		if 'file' not in request.files:
			flask('Error: File')
		file = request.files['file']
		if file.filename == "":
			flask('Error: No File Name')
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			prediction = new_model.predict(file)
			output = prediction
	return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)