import sqlite3

class FlightInfo:
    def __init__(self):
        self.db_path = 'airline.db'  # Update path if needed

    def setup_db(self):
        # Create table if not exists and insert sample data
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS flight (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                flight_number TEXT NOT NULL,
                origin TEXT NOT NULL,
                destination TEXT NOT NULL,
                departure_time TEXT NOT NULL,
                arrival_time TEXT NOT NULL
            )
        ''')
        # Insert sample data if table is empty
        cursor.execute("SELECT COUNT(*) FROM flight")
        count = cursor.fetchone()[0]
        if count == 0:
            sample_flights = [
                ("AI101", "Delhi", "Mumbai", "08:00", "10:00"),
                ("AI202", "Mumbai", "Bangalore", "11:00", "13:30"),
                ("AI303", "Bangalore", "Kolkata", "14:00", "17:00")
            ]
            cursor.executemany("INSERT INTO flight (flight_number, origin, destination, departure_time, arrival_time) VALUES (?, ?, ?, ?, ?)", sample_flights)
            conn.commit()
        conn.close()

    def show_flights(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM flight")
            rows = cursor.fetchall()
            if rows:
                print("\n--- FLIGHT INFORMATION ---")
                print(" | ".join([desc[0] for desc in cursor.description]))
                for row in rows:
                    print(" | ".join(str(item) for item in row))
            else:
                print("No flight records found.")
            conn.close()
        except Exception as e:
            print("Error fetching flight information:", e)

    def run(self):
        self.setup_db()
        self.show_flights()

if __name__ == "__main__":
    FlightInfo().run()
