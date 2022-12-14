from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
