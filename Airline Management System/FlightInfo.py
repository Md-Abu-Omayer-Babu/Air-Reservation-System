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
                ("BG101", "Dhaka", "Chattogram", "07:00", "08:00"),
                ("BG202", "Dhaka", "Sylhet", "09:00", "10:00"),
                ("BG303", "Dhaka", "Cox's Bazar", "11:00", "12:15"),
                ("BG404", "Chattogram", "Jessore", "13:00", "14:00"),
                ("BG505", "Sylhet", "Barisal", "15:00", "16:30"),
                ("BG606", "Dhaka", "Rajshahi", "17:00", "18:00")
            ]
            cursor.executemany("INSERT INTO flight (flight_number, origin, destination, departure_time, arrival_time) VALUES (?, ?, ?, ?, ?)", sample_flights)
            conn.commit()
        conn.close()

    def show_flights(self):
        CYAN = '\033[96m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        RESET = '\033[0m'
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM flight")
            rows = cursor.fetchall()
            if rows:
                print(f"{CYAN}\n===== FLIGHT INFORMATION ====={RESET}")
                print(f"{YELLOW}" + " | ".join([desc[0] for desc in cursor.description]) + f"{RESET}")
                for row in rows:
                    print(" | ".join(str(item) for item in row))
            else:
                print(f"{RED}No flight records found.{RESET}")
            conn.close()
        except Exception as e:
            print(f"{RED}Error fetching flight information: {e}{RESET}")

    def run(self):
        self.setup_db()
        self.show_flights()

if __name__ == "__main__":
    FlightInfo().run()
