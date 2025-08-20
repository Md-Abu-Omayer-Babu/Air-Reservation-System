import sqlite3

class BoardingPass:
    def __init__(self):
        self.db_path = 'airline.db'  # Update path if needed

    def get_pnr(self):
        CYAN = '\033[96m'
        RESET = '\033[0m'
        pnr = input(f"{CYAN}Enter PNR: {RESET}")
        return pnr

    def fetch_details(self, pnr):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            # Example query, adjust table/column names as needed
            cursor.execute("SELECT name, nationality, src, dest, fname, fcode, date FROM tickets WHERE pnr = ?", (pnr,))
            result = cursor.fetchone()
            conn.close()
            return result
        except Exception as e:
            print("Error fetching boarding pass details:", e)
            return None

    def display_boarding_pass(self, details):
        CYAN = '\033[96m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        RESET = '\033[0m'
        if details:
            print(f"{CYAN}\n===== AIR INDIA BOARDING PASS ====={RESET}")
            print(f"{YELLOW}Name: {details[0]}{RESET}")
            print(f"{YELLOW}Nationality: {details[1]}{RESET}")
            print(f"{YELLOW}Source: {details[2]}{RESET}")
            print(f"{YELLOW}Destination: {details[3]}{RESET}")
            print(f"{YELLOW}Flight Name: {details[4]}{RESET}")
            print(f"{YELLOW}Flight Code: {details[5]}{RESET}")
            print(f"{YELLOW}Date: {details[6]}{RESET}")
        else:
            print(f"{RED}No details found for the given PNR.{RESET}")

    def run(self):
        CYAN = '\033[96m'
        RESET = '\033[0m'
        print(f"{CYAN}\n===== AIR INDIA - Boarding Pass ====={RESET}")
        pnr = self.get_pnr()
        details = self.fetch_details(pnr)
        self.display_boarding_pass(details)

if __name__ == "__main__":
    BoardingPass().run()
