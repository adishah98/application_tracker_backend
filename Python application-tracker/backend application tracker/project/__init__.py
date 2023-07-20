from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS, cross_origin

UPLOAD_FOLDER = os.path.join('../project/static')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
# CORS(app,resources={r"/*": {"origins": "*"}})
# CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'sessionData'
app.config['TESTING'] = True
app.config['PORT']=8000
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

db = SQLAlchemy(app)


@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response

@app.route('/')
def index():
    return 'message'

import project.com  
