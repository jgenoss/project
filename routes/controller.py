from flask import Blueprint,render_template,Flask,url_for
from flask_login import LoginManager

controller = Blueprint('controller',__name__)

@controller.route('/')
def index():
    return render_template('index.html')

#@controller.route('/login', methods=['GET', 'POST'])

#def login():
    