from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):

    def __init__(self, id, username, name, password) -> None:
        self.id = id
        self.username = username
        self.name = name
        self.password = password
        
    @classmethod    
    def get_username(self,db,username):
        result = db.fetch_one("SELECT * FROM usuario WHERE usuario = '{0}'".format(username))
        if result:
            return User(id=result[0], username=result[4], name=result[3], password=result[5])
        return None
    
    @classmethod
    def get_user_id(self,db,user_id):
        result = db.fetch_one("SELECT id_usuario, usuario FROM usuario WHERE id_usuario = '{0}'".format(user_id))
        if result != None:
            return result[0]
        else:
            return None
            
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    