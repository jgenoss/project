from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from db_manager import db_manager

class User(UserMixin):

    def __init__(self, id, username, name, email, password) -> None:
        self.id = id
        self.username = username
        self.name = name
        self.email = email
        self.password = password
        #self.is_active = is_active
        #self.is_admin = is_admin
        
    @classmethod    
    def get_username(self,username):
        db = db_manager()
        result = db.fetch_one("SELECT id, username, password, name, email, is_active, is_admin FROM usuario WHERE username = '{0}'".format(username))
        if result:
            return User(id=result[0], username=result[1], password=result[2], name= result[3], email= result[4])
        else:
            return None
    
    @classmethod    
    def get(self,user_id):
        db = db_manager()
        result = db.fetch_one("SELECT id, username, password, name, email, is_active, is_admin FROM usuario WHERE id = '{0}'".format(user_id))
        if result:
            return User(id=result[0], username=result[1], password=result[2], name= result[3], email= result[4])
        else:
            return None
    
    @classmethod
    def get_user_id(self,user_id):
        db = db_manager()
        result = db.fetch_one("SELECT id, username, password, name, email, is_active, is_admin FROM usuario WHERE id = '{0}'".format(user_id))
        if result != None:
            return int(result[0])
        else:
            return None
        
    @classmethod   
    def is_validate(self,user_id):
        if self.get_user_id(user_id) == int(user_id):
            return self.get(user_id)
        return None
            
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
