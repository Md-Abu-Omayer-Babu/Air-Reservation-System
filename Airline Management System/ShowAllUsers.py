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
        # Ensure 'passenger' table exists for Bangladeshi context
        cursor.execute('''CREATE TABLE IF NOT EXISTS passenger (
            name TEXT, nationality TEXT, phone TEXT, address TEXT, nid TEXT, gender TEXT
        )''')
        cursor.execute("SELECT name, nationality, phone, address, nid, gender FROM passenger")
        rows = cursor.fetchall()
        if not rows:
            print(f"{RED}No passenger data found.{RESET}")
            return
        print(f"{CYAN}\n===== ALL PASSENGER DETAILS (Bangladesh) ====={RESET}")
        print(f"{YELLOW}Name | Nationality | Mobile | Address | NID | Gender{RESET}")
        for row in rows:
            print(" | ".join(str(item) for item in row))
    except Exception as e:
        print(f"{RED}Error fetching passenger data: {e}{RESET}")
    finally:
        conn.close()

if __name__ == "__main__":
    show_all_users()
