import os
import time
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, g, session
from flask_script import Manager
from werkzeug.utils import secure_filename

from utils import get_similar_images

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "a secret key"
manager = Manager(app)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = int(time.time())
            save_path = os.path.join(os.path.dirname(__file__), app.config['UPLOAD_FOLDER'], str(timestamp), filename)
            os.makedirs(os.path.join(os.path.dirname(__file__), app.config['UPLOAD_FOLDER'], str(timestamp)))
            file.save(save_path)
            return_list = get_similar_images(os.path.dirname(save_path))
            session["return_list"] = return_list
            return redirect(url_for('result_handler'))
        else:
            session["filename"] = file.filename
            return redirect(url_for('error_handler'))
    return render_template("upload_file.html")


@app.route('/results')
def result_handler():
    return render_template("return_images.html", return_list=session["return_list"])


@app.route('/error')
def error_handler():
    return render_template("error.html", filename=session["filename"])


@app.route('/image/<filename>')
def image_info(filename):
    return send_from_directory("images", filename)


if __name__ == '__main__':
    manager.run()
