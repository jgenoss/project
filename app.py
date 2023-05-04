from flask import Flask,session,redirect,url_for,flash
from flask_socketio import SocketIO,emit
from routes.controller import controller
from flask_login import LoginManager,current_user
from flask_session import Session

app = Flask(__name__)
socketio = SocketIO(app)
login_manager = LoginManager(app)
app.config['SESSION_TYPE'] = 'filesystem'
login_manager.login_view = 'controller.index'
login_manager.init_app(app)
Session(app)

app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000

app.register_blueprint(controller)

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    
@login_manager.user_loader
def load_user(user_id):
    from models.user import User
    return User.is_validate(user_id)


if __name__ == "__main__":
    socketio.run(
        app,
        port=app.config['PORT'],
        host=app.config['HOST']
    )