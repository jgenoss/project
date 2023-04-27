from flask import Flask,render_template,Blueprint,redirect,url_for
from flask_socketio import SocketIO,emit
from routes.controller import controller
from flask_login import LoginManager, login_user, logout_user, login_required
from models.db import db_manager
from models.user import User

app = Flask(__name__)
socketio = SocketIO(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000
db = db_manager()

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
    return User.get_user_id(db,user_id)
    
if __name__ == "__main__":
    socketio.run(
        app,
        port=app.config['PORT'],
        host=app.config['HOST']
    )