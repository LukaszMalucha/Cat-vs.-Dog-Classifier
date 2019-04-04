## App Utilities
import os
import env
from db import db

from flask_bootstrap import Bootstrap
from flask_restful import Api
from flask import Flask, render_template, current_app, request, redirect, url_for, flash, jsonify
from flask_uploads import UploadSet, configure_uploads, IMAGES

import numpy as np
import keras
import h5py
from keras.models import load_model

from skimage.io import imread
from skimage.transform import resize

from resources.user import UserRegister, UserLogin, UserLogout, login_manager

## App Settings

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
photos = UploadSet('photos', IMAGES)  # image upload handling
app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
configure_uploads(app, photos)

ALLOWED_EXTENSIONS = set(['jpg'])

app.config['DEBUG'] = True
api = Api(app)

Bootstrap(app)
login_manager.init_app(app)

## Register Resources

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')


### MAIN PAGE


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html")


## DEFINE ALLOWED TEMPLATE FILE FORMAT ##############################################   

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


### TEST PHOTO


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST' and 'file' in request.files:

        image = request.files['file']
        if allowed_file(image.filename):
            # clear Tensor session to avoid error
            keras.backend.clear_session()
            # load saved model
            image_classifier = load_model('image_classifier.h5')
            # prepare labels
            class_labels = {0: 'Cat', 1: 'Dog'}
            # read photo & transform it into array
            img = imread(image)
            img = resize(img, (128, 128))
            img = np.expand_dims(img, axis=0)
            if np.max(img) > 1:
                img = img / 255.0
            # predict class
            prediction = image_classifier.predict_classes(img)
            percent_values = prediction.tolist()
            # for website display
            guess = class_labels[prediction[0][0]]
            # clear Tensor session to avoid error
            # keras.backend.clear_session()

            return jsonify({'guess': guess})

        else:
            return jsonify({'error': "Only .jpg files allowed"})
    else:
        return jsonify({'error': "Please upload a .jpg file"})

### ERROR HANDLING


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500

## DB INIT
db.init_app(app)

## APP INITIATION
if __name__ == '__main__':

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run()

## Heroku
# port = int(os.environ.get('PORT', 5000))
# app.run(host='0.0.0.0', port=port)
