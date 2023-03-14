import mysql.connector

class DatabaseController:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(buffered=True)
    
    def execute(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except mysql.connector.Error as error:
            print("Error: {}".format(error))
    
    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def fetch_one(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def close(self):
        self.cursor.close()
        self.conn.close()
