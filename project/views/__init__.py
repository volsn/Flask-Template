from flask import Blueprint

core = Blueprint('core', __name__)


@core.route('/')
def index():
    return 'Hello world'
