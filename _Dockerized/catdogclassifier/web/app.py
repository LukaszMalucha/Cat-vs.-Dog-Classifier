## App Utilities
import os
import env
from db import db

from flask_bootstrap import Bootstrap
from flask_restful import Api
from flask import Flask, render_template, request, jsonify
from flask_uploads import UploadSet, configure_uploads, IMAGES

from resources.user import UserRegister, UserLogin, UserLogout, login_manager
from resources.utils import allowed_file, image_classification

## App Settings

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
app.config['FLASKS3_BUCKET_NAME'] = os.environ.get('FLASKS3_BUCKET_NAME')
photos = UploadSet('photos', IMAGES)  # image upload handling
configure_uploads(app, photos)

app.config['DEBUG'] = True
api = Api(app)

Bootstrap(app)
login_manager.init_app(app)

## Register Resources

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')




@app.route('/', methods=['GET', 'POST'])
def dashboard():
    """Main Dashboard"""
    return render_template("dashboard.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Image Classification"""
    if request.method == 'POST' and 'file' in request.files:
        image = request.files['file']
        # .jpg file extension check
        if allowed_file(image.filename):
            # Apply neural network
            guess = image_classification(image)

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

    app.run(host='0.0.0.0')        
	