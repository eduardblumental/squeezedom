import os
from flask import Flask

app = Flask(__name__, template_folder="..\\templates", static_folder="..\\static")

app.config['UPLOADED_FOLDER'] = os.path.join(os.getcwd(), 'uploaded')
app.config['PROCESSED_FOLDER'] = os.path.join(os.getcwd(), 'processed')

from app import routes
