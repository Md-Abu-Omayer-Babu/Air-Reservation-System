import sqlite3
from Conn import Conn

def show_all_users():
    conn = Conn().get_connection()
    if not conn:
        print("Failed to connect to database.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")  # Change 'users' to your actual table name
        rows = cursor.fetchall()
        if not rows:
            print("No user data found.")
            return
        print("All User Details:")
        for row in rows:
            print(row)
    except Exception as e:
        print("Error fetching user data:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    show_all_users()
