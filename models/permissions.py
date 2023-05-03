from db_manager import db_manager

@classmethod
class Role:
    def __init__(self, name):
        self.name = name
        
@classmethod
class Permission:
    def __init__(self, name):
        self.name = [name]
              
class RolePermissions:
    def __init__(self):
        self.db = db_manager()

    def __del__(self):
        self.db.close()
        
    def get_user_permissions(self, username):
        rtn = self.db.fetch_all(f"""
            SELECT
                p.nombre 
            FROM
                permisos p
                INNER JOIN roles_permisos rp ON p.id_permiso = rp.id_permiso
                INNER JOIN usuario u ON u.id_rol = rp.id_rol 
            WHERE
                u.username = '{username}""")
        return [Permission([r]) for r in rtn]

    def get_user_roles(self, username):
        results = self.db.fetch_one(f"""
            SELECT
                r.nombre 
            FROM
                roles r
                INNER JOIN usuario u ON u.id_rol = r.id_rol 
            WHERE
                u.username = '{username}'""")
        return [Role(results[0])]

    def get_role_permissions(self, role_name):
        results = self.db.fetch_one(f"""
            SELECT
                p.nombre 
            FROM
                permisos p
                INNER JOIN roles_permisos rp ON p.id_permiso = rp.id_permiso
                INNER JOIN roles r ON r.id_rol = rp.id_rol 
            WHERE
                r.nombre = '{role_name}'""")
        return [Permission(results[0])]