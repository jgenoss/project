from flask import Flask, render_template,redirect,url_for,session,request
import os, sys
from pprint import pprint
from controller.DatabaseController import DatabaseController

class MyApp(Flask):
    def __init__(self,name):
        super(MyApp,self).__init__(name)
        self.config['SECRET_KEY'] = os.urandom(25)
        self.config['DEBUG'] = True
        self.routes()
        try:
            self.db = DatabaseController(
                host='localhost',
                user='root',
                password='',
                database='db_deca'
            )
        except Exception as err:
            print(err)
        
    
    def routes(self):
        def viewIndex():
            return render_template('index.html')
        self._url('/',viewIndex,['GET'])
        self._url('/index',viewIndex,['GET'])
        
        def Viewlogin():
            return render_template('login.html')
        self._url('/login',Viewlogin,['GET'])
    
    def _url(self,url,func,methods):
           self.add_url_rule(url,view_func=func,methods=methods)
           
app = MyApp(__name__)
    
if __name__ == '__main__':
    app.run()