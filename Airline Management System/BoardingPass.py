import sqlite3

class BoardingPass:
    def __init__(self):
        self.db_path = 'airline.db'  # Update path if needed

    def get_pnr(self):
        pnr = input("Enter PNR: ")
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
        if details:
            print("\n--- AIR INDIA BOARDING PASS ---")
            print(f"Name: {details[0]}")
            print(f"Nationality: {details[1]}")
            print(f"Source: {details[2]}")
            print(f"Destination: {details[3]}")
            print(f"Flight Name: {details[4]}")
            print(f"Flight Code: {details[5]}")
            print(f"Date: {details[6]}")
        else:
            print("No details found for the given PNR.")

    def run(self):
        print("AIR INDIA - Boarding Pass")
        pnr = self.get_pnr()
        details = self.fetch_details(pnr)
        self.display_boarding_pass(details)

if __name__ == "__main__":
    BoardingPass().run()
