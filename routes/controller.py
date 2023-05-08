from flask import Blueprint,render_template,url_for,request,redirect,session,flash
from flask_login import login_user, logout_user, login_required, UserMixin,current_user,confirm_login
from functools import wraps

controller = Blueprint('controller',__name__)

def require_permissions(roles=[], permissions=[]):
    from models.user import User
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'username' not in session:
                return redirect(url_for('controller.login'))
            
            # Verificar si el usuario tiene los roles necesarios
            user_roles = set(User.get_user_roles(session['username']))
            if not user_roles.issubset(roles):
                flash('No tiene permisos para acceder a esta página','error')
                return redirect(url_for('controller.error', message="R No tiene permisos para acceder a esta página."))
            
            # Verificar si el usuario tiene los permisos necesarios
            user_permissions = set(User.get_user_permissions(session['username']))
            if not user_permissions.issubset(permissions):
                flash('No tiene permisos para acceder a esta página','error')
                return redirect(url_for('controller.error', message="P No tiene permisos para acceder a esta página."))

            
            # Si todo está bien, ejecutar la función
            return func(*args, **kwargs)
        return wrapper
    return decorator

@controller.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('error404'))

@controller.route('/error')
def error():
    message = request.args.get('message', 'Ha ocurrido un error.')
    return render_template('error.html', message=message)

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
        return redirect(url_for('controller.home'))

@controller.route('/submit_login', methods=['GET','POST'])
def submit_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        from models.user import User
        logger_user = User.get_username(username)
        if logger_user and logger_user.password == password:
            session['is_session'] = 1
            session['username'] = logger_user.username
            session['user_id'] = logger_user.id
            print(logger_user.id)
            login_user(logger_user)
            return redirect(url_for('controller.home'))
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
@require_permissions(['Admin','Editor','Lector'],['Leer'])
def dashboard():
    return render_template('modulos/dashboard.html')

@controller.route('/clientes')
@login_required
@require_permissions(['Admin','Editor','Lector'],['Leer'])
def clientes():
    return render_template('modulos/clientes.html')

@controller.route('/bodegas')
@login_required
@require_permissions(['Admin','Editor','Lector'],['Leer'])
def bodegas():
    return render_template('modulos/bodegas.html')

@controller.route('/usuarios')
@login_required
@require_permissions(['Admin','Editor','Lector'],['Leer'])
def usuarios():
    return render_template('modulos/usuarios.html')

@controller.route('/productos')
@login_required
@require_permissions(['Admin','Editor','Lector'],['Leer'])
def productos():
    return render_template('modulos/productos.html')