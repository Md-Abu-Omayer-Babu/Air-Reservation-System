import sqlite3
import uuid

class BookFlight:
    def __init__(self):
        self.db_path = 'airline.db'  # Update path if needed

    def get_aadhar(self):
        aadhar = input("Enter Aadhar Number: ")
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
        source = input("Source: ")
        destination = input("Destination: ")
        fname = input("Flight Name: ")
        fcode = input("Flight Code: ")
        date = input("Date (YYYY-MM-DD): ")
        return source, destination, fname, fcode, date

    def book_flight(self, aadhar, user_details, flight_details):
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
            print(f"Flight booked successfully! Your PNR is: {pnr}")
        except Exception as e:
            print("Error booking flight:", e)

    def run(self):
        print("Book Flight")
        aadhar = self.get_aadhar()
        user_details = self.fetch_user(aadhar)
        if user_details:
            print(f"Name: {user_details[0]}")
            print(f"Nationality: {user_details[1]}")
            print(f"Address: {user_details[2]}")
            print(f"Gender: {user_details[3]}")
            flight_details = self.get_flight_details()
            self.book_flight(aadhar, user_details, flight_details)
        else:
            print("No user found with the given Aadhar number.")

if __name__ == "__main__":
    BookFlight().run()
