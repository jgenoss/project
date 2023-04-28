import mysql.connector

class db_manager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='test'
        )
        self.cursor = self.conn.cursor(buffered=True)
    
    def execute(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            return self.cursor.lastrowid
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
