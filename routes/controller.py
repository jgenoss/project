from flask import Blueprint,render_template,url_for,request,redirect,session
from flask_login import login_user, logout_user, login_required, UserMixin,current_user,confirm_login

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
    if 'is_session' not in session:
        return render_template('login.html')
    else:
        return redirect(url_for('controller.dashboard'))

@controller.route('/submit_login', methods=['GET','POST'])
def submit_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        from models.user import User
        logger_user = User.get_username(username)
        #print(User.get_username(username))
        if logger_user and logger_user.password == password:
            session['is_session'] = 1
            login_user(logger_user)
            return redirect(url_for('controller.dashboard'))
        else:
            return render_template('login.html', message='El nombre de usuario o contraseña son inválidos')
    else:
        return redirect(url_for('controller.login'))

@controller.route('/logout')
def logout():
    logout_user()
    session.pop("is_session",None)
    return redirect(url_for('controller.login'))

@controller.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')