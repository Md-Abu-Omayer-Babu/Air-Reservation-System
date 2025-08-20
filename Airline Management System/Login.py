import sqlite3

class Login:
    def __init__(self):
        self.db_path = 'airline.db'  # Update path if needed

    def get_credentials(self):
        username = input("Username: ")
        password = input("Password: ")
        return username, password

    def check_login(self, username, password):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM login WHERE username = ? AND password = ?", (username, password))
            result = cursor.fetchone()
            conn.close()
            return result is not None
        except Exception as e:
            print("Error checking login:", e)
            return False

    def run(self):
        print("Login")
        while True:
            username, password = self.get_credentials()
            if self.check_login(username, password):
                print("Login successful!")
                break
            else:
                print("Invalid username or password. Try again.")
            action = input("Type 'reset' to clear, 'close' to exit, or press Enter to try again: ").lower()
            if action == 'reset':
                continue
            elif action == 'close':
                print("Exiting login.")
                break

if __name__ == "__main__":
    Login().run()
