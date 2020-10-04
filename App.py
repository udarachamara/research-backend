from flask import Flask, send_from_directory, request
from flask_cors import CORS
from flask_restful import Api
import secrets
import os
import RestApi

UPLOAD_FOLDER = 'uploads'
OUT_FOLDER = 'out'
ALLOWED_EXTENSIONS = {'wav'}
app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api.add_resource(RestApi, '/api')  # Route_Default


@app.route('/api/uploadFile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        f_token = secrets.token_hex(5)
        filename = f_token + '_' + file.filename
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return {'status': 'Upload working..!',
                    'data': filename,
                    'response_code': 1001,
                    'Application': 'Research 2020-159-speech_recognition_system',
                    'version': '1.0.0'}
        else:
            return {'status': 'No file Or File Format Not Supported..!',
                    'response_code': 1002,
                    'Application': 'Research 2020-159-speech_recognition_system',
                    'version': '1.0.0'}

    else:
        return {'status': 'No Post method..!',
                'response_code': 1003,
                'Application': 'Research 2020-159-speech_recognition_system',
                'version': '1.0.0'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
