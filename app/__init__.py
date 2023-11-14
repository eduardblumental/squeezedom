import os
from flask import Flask

app = Flask(__name__, template_folder="..\\templates", static_folder="..\\static")
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import routes
