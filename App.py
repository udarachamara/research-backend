from flask import Flask, send_from_directory, request, send_file
from flask_cors import CORS
from flask_restful import Api
import secrets
import os

UPLOAD_FOLDER = 'uploads'
OUT_FOLDER = 'out'
ALLOWED_EXTENSIONS = {'wav'}
app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/api', methods=['GET'])
def test_api():
    return {'status': 'Server working..!',
            'response_code': 200,
            'Application': 'Research 2020-159-speech_recognition_system',
            'version': '1.0.0'}


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


@app.route('/api/processNoise/<filename>', methods=['GET'])
def process_noise(filename):
    file_path = OUT_FOLDER+"/" + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')
    # return {'status': 'Upload working..!',
    #         'data': "",
    #         'response_code': 1001,
    #         'Application': 'Research 2020-159-speech_recognition_system',
    #         'version': '1.0.0'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')
