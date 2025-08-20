import sqlite3

class Login:
    def __init__(self):
        self.db_path = 'airline.db'  # Update path if needed

    def get_credentials(self):
        CYAN = '\033[96m'
        YELLOW = '\033[93m'
        RESET = '\033[0m'
        username = input(f"{YELLOW}Username: {RESET}")
        password = input(f"{YELLOW}Password: {RESET}")
        return username, password

    def check_login(self, username, password):
        RED = '\033[91m'
        RESET = '\033[0m'
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM login WHERE username = ? AND password = ?", (username, password))
            result = cursor.fetchone()
            conn.close()
            return result is not None
        except Exception as e:
            print(f"{RED}Error checking login: {e}{RESET}")
            return False

    def run(self):
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        RED = '\033[91m'
        RESET = '\033[0m'
        print(f"{CYAN}\n===== LOGIN ====={RESET}")
        while True:
            username, password = self.get_credentials()
            if self.check_login(username, password):
                print(f"{GREEN}\u2705 Login successful!{RESET}")
                break
            else:
                print(f"{RED}Invalid username or password. Try again.{RESET}")
            action = input(f"{CYAN}Type 'reset' to clear, 'close' to exit, or press Enter to try again: {RESET}").lower()
            if action == 'reset':
                continue
            elif action == 'close':
                print(f"{CYAN}Exiting login.{RESET}")
                break

if __name__ == "__main__":
    Login().run()
