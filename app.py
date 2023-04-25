from flask import Flask,render_template,Blueprint
from flask_socketio import SocketIO,emit
from routes.controller import controller
from flask_login import LoginManager,UserMixin

app = Flask(__name__)
socketio = SocketIO(app)
login_manager = LoginManager(app)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

app.register_blueprint(controller)

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
    socketio.run(
        app,
        port=8000,
        host='0.0.0.0'
    )