import sqlite3

class JourneyDetails:
    def __init__(self):
        self.db_path = 'airline.db'  # Update path if needed

    def get_pnr(self):
        pnr = input("Enter PNR Number: ")
        return pnr

    def show_details(self, pnr):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tickets WHERE pnr = ?", (pnr,))
            rows = cursor.fetchall()
            if rows:
                print("\n--- JOURNEY DETAILS ---")
                print(" | ".join([desc[0] for desc in cursor.description]))
                for row in rows:
                    print(" | ".join(str(item) for item in row))
            else:
                print("No Information Found for the given PNR.")
            conn.close()
        except Exception as e:
            print("Error fetching journey details:", e)

    def run(self):
        print("Journey Details")
        pnr = self.get_pnr()
        self.show_details(pnr)

if __name__ == "__main__":
    JourneyDetails().run()
