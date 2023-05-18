from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_socketio import SocketIO, emit
from flask_login import LoginManager, current_user,login_user, logout_user, login_required, UserMixin, confirm_login
from flask_session import Session
from models.user import User
from functools import wraps
from pprint import pprint

class App(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SESSION_TYPE'] = 'filesystem'
        self.app.config['SECRET_KEY'] = 'secret!'
        self.app.config['DEBUG'] = True
        self.app.config['HOST'] = '0.0.0.0'
        self.app.config['PORT'] = 5000
        self.socketio = SocketIO(self.app)
        self.login_manager = LoginManager(self.app)
        self.session = Session(self.app)
        self.login_manager.login_view = 'index'
        self.login_manager.user_loader(self.load_user)

        self.app.add_url_rule('/', view_func=self.index)
        self.app.add_url_rule('/login', view_func=self.login)
        self.app.add_url_rule('/submit_login', methods=['GET', 'POST'], view_func=self.submit_login)
        self.app.add_url_rule('/logout', view_func=self.logout)
        self.app.add_url_rule('/dashboard', view_func=self.dashboard)
        self.app.add_url_rule('/clientes', view_func=self.clientes)
        self.app.add_url_rule('/bodegas', view_func=self.bodegas)
        self.app.add_url_rule('/usuarios', view_func=self.usuarios)
        self.app.add_url_rule('/productos', view_func=self.productos)
        self.app.add_url_rule('/error', view_func=self.error)
        
        self.socketio.on_event('message', self.handle_message)
        
    def handle_message(self, data):
        print('received message: ' + str(data))
    
    def handle_open_table(self, data):
        print('received message: ' + str(data))
        
    def require_permissions(roles=[], permissions=[]):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if 'username' not in session:
                    return redirect(url_for('login'))

                # Verificar si el usuario tiene los roles necesarios
                user_roles = set(User.get_user_roles(session['username']))
                if not user_roles.issubset(roles):
                    flash('No tiene permisos para acceder a esta página','error')
                    return redirect(url_for('dashboard'))

                # Verificar si el usuario tiene los permisos necesarios
                user_permissions = set(User.get_user_permissions(session['username']))
                print(user_permissions)
                if not user_permissions.issubset(permissions):
                    flash('No tiene permisos para acceder a esta página','error')
                    return redirect(url_for('dashboard'))

                # Si todo está bien, ejecutar la función
                return func(*args, **kwargs)
            return wrapper
        return decorator 
        
    def load_user(self, user_id):
        return User.is_validate(user_id)

    def index(self):
        return redirect(url_for('login'))

    def login(self):
        if 'is_session' not in session:
            return render_template('login.html')
        else:
            return redirect(url_for('dashboard'))


    def submit_login(self):
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            logger_user = User.get_username(username)
            if logger_user and logger_user.password == password:
                session['is_session'] = 1
                session['username'] = logger_user.username
                session['user_id'] = logger_user.id
                login_user(logger_user)
                return redirect(url_for('dashboard'))
            else:
                return render_template('login.html', message='El nombre de usuario o contraseña son inválidos')
        else:
            return redirect(url_for('login'))

    def error(self):
        message = request.args.get('message', 'Ha ocurrido un error.')
        return render_template('error.html', message=message)

    def logout(self):
        logout_user()
        session.pop("is_session", None)
        return redirect(url_for('login'))


    @login_required
    def dashboard(self):
        return render_template('modulos/dashboard.html')


    @login_required
    @require_permissions(roles=['Admin', 'Editor', 'Lector'], permissions=['Leer'])
    def clientes(self):
        return render_template('modulos/clientes.html')


    @login_required
    @require_permissions(roles=['Admin', 'Editor', 'Lector'], permissions=['Leer'])
    def bodegas(self):
        return render_template('modulos/bodegas.html')


    @login_required
    @require_permissions(roles=['Admin', 'Editor', 'Lector'], permissions=['Leer'])
    def usuarios(self):
        return render_template('modulos/usuarios.html')


    @login_required
    @require_permissions(roles=['Admin', 'Editor', 'Lector'], permissions=['Leer'])
    def productos(self):
        return render_template('modulos/productos.html')
    
    def run(self):
        self.socketio.run(
            self.app,
            port=self.app.config['PORT'],
            host=self.app.config['HOST']
        )

if __name__ == "__main__":
    app = App()
    app.run()