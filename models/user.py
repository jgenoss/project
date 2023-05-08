from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from db_manager import db_manager
from pprint import pprint

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
        result = db.fetch_one("SELECT id, username, password, name, email FROM usuario WHERE username = '{0}'".format(username))
        if result:
            return User(id=result[0], username=result[1], password=result[2], name= result[3], email= result[4])
        else:
            return None
        
    @classmethod    
    def get(self,user_id):
        db = db_manager()
        result = db.fetch_one("SELECT id, username, password, name, email FROM usuario WHERE id = '{0}'".format(user_id))
        if result:
            return User(id=result[0], username=result[1], password=result[2], name= result[3], email= result[4])
        else:
            return None
    
    @classmethod
    def get_user_id(self,user_id):
        db = db_manager()
        result = db.fetch_one("SELECT id, username, password, name, email FROM usuario WHERE id = '{0}'".format(user_id))
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

    @classmethod
    def get_user_roles(self, username):
        db = db_manager()
        rtn = db.fetch_one(f"""
            SELECT
                r.nombre 
            FROM
                roles r
                INNER JOIN usuario u ON r.id_rol = u.id_rol 
            WHERE
                u.username = '{username}'""")
        return [rtn[0]]
    
    @classmethod
    def get_user_permissions(self,user_id):
        db = db_manager()
        results = db.fetch_all(f"""
            SELECT
                permisos.nombre 
            FROM
                roles
                INNER JOIN roles_permisos ON roles.id_rol = roles_permisos.id_rol
                INNER JOIN usuario ON roles.id_rol = usuario.id_rol
                INNER JOIN permisos ON roles_permisos.id_permiso = permisos.id_permiso 
            WHERE
                usuario.id = '{user_id}'""")
        return [r[0] for r in results]