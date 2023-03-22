from DatabaseController import DatabaseController
class User(object):
    def __init__(self):
        try:
            self.db = DatabaseController(
                host='localhost',
                user='root',
                password='',
                database='db_deca'
            )
        except Exception as err:
            print(err)
    
    def _login_user(self,data):
        user = data[0]
        password = data[1]
        self.db.fetch_one(f"select from usuario where usuario = '{user}'and contrasena = {password}")
        return(f"login user {data}")
        
    def _new_user(self,data):
        print("new user")
        
    def _edit_user(self,data):
        print("edit user")
    
    def _change_pass(self,data):
        print("change pass")
        
    def _change_mail(self,data):
        print("change mail")