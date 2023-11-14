import os

from flask import render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from app import app

import model


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        print(file)
        if not file or file.filename == '':
            return redirect(request.url)

        image_name = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
        image_name = model.image_to_png(app.config['UPLOAD_FOLDER'], image_name)
        return redirect(url_for('success', filename=image_name))

    return render_template('upload.html')


@app.route('/success/<filename>')
def success(filename):
    return render_template('success.html', filename=filename)


@app.route('/uploads/<filename>')
def render_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/processed_images')
def processed_images():
    image_names = [f for f in os.listdir(app.config['UPLOAD_FOLDER'])]
    return render_template('processed_images.html', image_names=image_names)
