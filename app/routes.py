import os

from flask import render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from app.utils import allowed_file
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('success', filename=filename))
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
