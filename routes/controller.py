from flask import Blueprint,render_template,Flask,url_for,request,redirect
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from flask_session import Session
from models.user import User
from models.db import db_manager

db = db_manager()

controller = Blueprint('controller',__name__)

@controller.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('error404'))

@controller.route('/error404')
def error404():
    # Renderiza la página de error 404
    return render_template('500.html')

@controller.route('/')
def index():
    return redirect(url_for('controller.login'))

@controller.route('/login')
def login():
    return render_template('login.html')

@controller.route('/submit_login', methods=['GET','POST'])
def submit_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        logger_user = User.get_username(db,username)
        
        if logger_user != None and logger_user.password == password:
            login_user(logger_user)
            return redirect(url_for('controller.dashboard'))
        else:
            return render_template(
                'login.html', 
                error='El nombre de usuario o contraseña son inválidos'
            )
    else:
        return redirect(url_for('controller.login'))

@controller.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')