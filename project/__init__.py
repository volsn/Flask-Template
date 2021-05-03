import os
from dotenv import load_dotenv
from flask import Flask


"""
App Setup
"""

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


"""
Blueprint Registration
"""

from project.views import core

app.register_blueprint(core)
