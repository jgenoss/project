from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from db_manager import db_manager
from pprint import pprint

class User(UserMixin):
    def __init__(self, id, username, name, email, password):
        self.id = id
        self.username = username
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def get_username(cls, username):
        db = db_manager()
        result = db.fetch_one("SELECT id, username, name, email, password FROM usuario WHERE username = %s",(username,))
        if result:
            return cls(*result)
        else:
            return None

    @classmethod
    def get(cls, user_id):
        db = db_manager()
        result = db.fetch_one("SELECT id, username, password, name, email FROM usuario WHERE id = %s",(user_id,))
        if result:
            return cls(*result)
        else:
            return None

    @classmethod
    def get_user_id(cls, user_id):
        db = db_manager()
        result = db.fetch_one("SELECT id, username, password, name, email FROM usuario WHERE id = %s",(user_id,))
        if result is not None:
            return int(result[0])
        else:
            return None

    @classmethod
    def is_validate(cls, user_id):
        if cls.get_user_id(user_id) == int(user_id):
            return cls.get(user_id)
        return None

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @classmethod
    def get_user_roles(cls, username):
        db = db_manager()
        rtn = db.fetch_one("SELECT r.nombre FROM roles r INNER JOIN usuario u ON r.id_rol = u.id_rol WHERE u.username = %s ",(username,))
        return [rtn[0]]

    @classmethod
    def get_user_permissions(cls, user_id):
        db = db_manager()
        results = db.fetch_all("SELECT permisos.nombre FROM roles INNER JOIN roles_permisos ON roles.id_rol = roles_permisos.id_rol INNER JOIN usuario ON roles.id_rol = usuario.id_rol INNER JOIN permisos ON roles_permisos.id_permiso = permisos.id_permiso WHERE usuario.id = %s",(user_id,))
        return [r[0] for r in results]