from flask import Flask,render_template,Blueprint,redirect,url_for
from flask_socketio import SocketIO,emit
from routes.controller import controller
#from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

app = Flask(__name__)
socketio = SocketIO(app)
#login_manager = LoginManager(app)
#login_manager.init_app(app)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000

#def load_user(user_id):
#    from models.user import User
#    return User.get_id(user_id)



@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('error404'))

@app.route('/error404')
def error404():
    # Renderiza la página de error 404
    return render_template('500.html')

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
        port=app.config['PORT'],
        host=app.config['HOST']
    )