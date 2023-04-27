from flask import Blueprint,render_template,Flask,url_for,request,redirect
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

controller = Blueprint('controller',__name__)


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
        if username == 'jose' and password == '1234':
            return redirect(url_for('controller.dashboard'))
        else:
            return render_template(
                'login.html', 
                error='El nombre de usuario o contraseña son inválidos'
            )
    else:
        return redirect(url_for('controller.login'))

@controller.route('/dashboard')
#@login_required
def dashboard():
    return render_template('dashboard.html')