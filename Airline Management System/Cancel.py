import sqlite3
import uuid

class Cancel:
    def __init__(self):
        self.db_path = 'airline.db'  # Update path if needed

    def get_pnr(self):
        pnr = input("Enter PNR Number: ")
        return pnr

    def fetch_ticket(self, pnr):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name, fcode, date FROM tickets WHERE pnr = ?", (pnr,))
            result = cursor.fetchone()
            conn.close()
            return result
        except Exception as e:
            print("Error fetching ticket details:", e)
            return None

    def cancel_ticket(self, pnr):
        cancellation_no = str(uuid.uuid4())[:8]
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tickets WHERE pnr = ?", (pnr,))
            conn.commit()
            conn.close()
            print(f"Ticket cancelled successfully! Cancellation No: {cancellation_no}")
        except Exception as e:
            print("Error cancelling ticket:", e)

    def run(self):
        print("CANCELLATION")
        pnr = self.get_pnr()
        ticket = self.fetch_ticket(pnr)
        if ticket:
            print(f"Name: {ticket[0]}")
            print(f"Flight Code: {ticket[1]}")
            print(f"Date of Travel: {ticket[2]}")
            confirm = input("Do you want to cancel this ticket? (yes/no): ")
            if confirm.lower() == "yes":
                self.cancel_ticket(pnr)
            else:
                print("Cancellation aborted.")
        else:
            print("No ticket found for the given PNR.")

if __name__ == "__main__":
    Cancel().run()
