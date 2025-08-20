import sqlite3
import uuid

class BookFlight:
    def __init__(self):
        self.db_path = 'airline.db'  # Update path if needed

    def get_aadhar(self):
        CYAN = '\033[96m'
        RESET = '\033[0m'
        aadhar = input(f"{CYAN}Enter Aadhar Number: {RESET}")
        return aadhar

    def fetch_user(self, aadhar):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name, nationality, address, gender FROM passenger WHERE aadhar = ?", (aadhar,))
            result = cursor.fetchone()
            conn.close()
            return result
        except Exception as e:
            print("Error fetching user details:", e)
            return None

    def get_flight_details(self):
        YELLOW = '\033[93m'
        RESET = '\033[0m'
        source = input(f"{YELLOW}Source: {RESET}")
        destination = input(f"{YELLOW}Destination: {RESET}")
        fname = input(f"{YELLOW}Flight Name: {RESET}")
        fcode = input(f"{YELLOW}Flight Code: {RESET}")
        date = input(f"{YELLOW}Date (YYYY-MM-DD): {RESET}")
        return source, destination, fname, fcode, date

    def book_flight(self, aadhar, user_details, flight_details):
        GREEN = '\033[92m'
        RED = '\033[91m'
        RESET = '\033[0m'
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS tickets (
                aadhar TEXT, name TEXT, nationality TEXT, address TEXT, gender TEXT,
                src TEXT, dest TEXT, fname TEXT, fcode TEXT, date TEXT, pnr TEXT)''')
            pnr = str(uuid.uuid4())[:8]
            cursor.execute(
                "INSERT INTO tickets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (aadhar, user_details[0], user_details[1], user_details[2], user_details[3],
                 flight_details[0], flight_details[1], flight_details[2], flight_details[3], flight_details[4], pnr)
            )
            conn.commit()
            conn.close()
            print(f"{GREEN}\u2705 Flight booked successfully! Your PNR is: {pnr}{RESET}")
        except Exception as e:
            print(f"{RED}Error booking flight: {e}{RESET}")

    def run(self):
        CYAN = '\033[96m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        RESET = '\033[0m'
        print(f"{CYAN}\n===== BOOK FLIGHT ====={RESET}")
        aadhar = self.get_aadhar()
        user_details = self.fetch_user(aadhar)
        if user_details:
            print(f"{YELLOW}Name: {user_details[0]}{RESET}")
            print(f"{YELLOW}Nationality: {user_details[1]}{RESET}")
            print(f"{YELLOW}Address: {user_details[2]}{RESET}")
            print(f"{YELLOW}Gender: {user_details[3]}{RESET}")
            flight_details = self.get_flight_details()
            self.book_flight(aadhar, user_details, flight_details)
        else:
            print(f"{RED}No user found with the given Aadhar number.{RESET}")

if __name__ == "__main__":
    BookFlight().run()
