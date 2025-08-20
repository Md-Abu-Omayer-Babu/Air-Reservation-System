import sqlite3
from Conn import Conn

def show_all_users():
    conn = Conn().get_connection()
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    if not conn:
        print(f"{RED}Failed to connect to database.{RESET}")
        return
    cursor = conn.cursor()
    try:
        # Ensure 'users' table exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT,
            phone TEXT
        )''')
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        if not rows:
            print(f"{RED}No user data found.{RESET}")
            return
        print(f"{CYAN}\n===== ALL USER DETAILS ====={RESET}")
        print(f"{YELLOW}" + " | ".join([desc[0] for desc in cursor.description]) + f"{RESET}")
        for row in rows:
            print(" | ".join(str(item) for item in row))
    except Exception as e:
        print(f"{RED}Error fetching user data: {e}{RESET}")
    finally:
        conn.close()

if __name__ == "__main__":
    show_all_users()
