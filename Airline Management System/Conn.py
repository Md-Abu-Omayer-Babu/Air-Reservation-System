import sqlite3

class Conn:
    def __init__(self, db_path='airline.db'):
        self.db_path = db_path

    def get_connection(self):
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except Exception as e:
            print("Error connecting to database:", e)
            return None

# Example usage:
# conn = Conn().get_connection()
# cursor = conn.cursor()
# ... perform queries ...
# conn.close()
