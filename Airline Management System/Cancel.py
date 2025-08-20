import sqlite3
import uuid

class Cancel:
    def __init__(self):
        self.db_path = 'airline.db'  # Update path if needed

    def get_pnr(self):
        CYAN = '\033[96m'
        RESET = '\033[0m'
        pnr = input(f"{CYAN}Enter PNR Number: {RESET}")
        return pnr

    def fetch_ticket(self, pnr):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name, src, dest, fcode, date FROM tickets WHERE pnr = ?", (pnr,))
            result = cursor.fetchone()
            conn.close()
            return result
        except Exception as e:
            print("Error fetching ticket details:", e)
            return None

    def cancel_ticket(self, pnr):
        GREEN = '\033[92m'
        RED = '\033[91m'
        RESET = '\033[0m'
        cancellation_no = str(uuid.uuid4())[:8]
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tickets WHERE pnr = ?", (pnr,))
            conn.commit()
            conn.close()
            print(f"{GREEN}\u274C Ticket cancelled successfully! Cancellation No: {cancellation_no}{RESET}")
        except Exception as e:
            print(f"{RED}Error cancelling ticket: {e}{RESET}")

    def run(self):
        CYAN = '\033[96m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        RESET = '\033[0m'
        print(f"{CYAN}\n===== CANCELLATION (Bangladesh) ====={RESET}")
        pnr = self.get_pnr()
        ticket = self.fetch_ticket(pnr)
        if ticket:
            print(f"{YELLOW}Passenger Name: {ticket[0]}{RESET}")
            print(f"{YELLOW}From: {ticket[1]}{RESET}")
            print(f"{YELLOW}To: {ticket[2]}{RESET}")
            print(f"{YELLOW}Flight Code: {ticket[3]}{RESET}")
            print(f"{YELLOW}Date of Travel: {ticket[4]}{RESET}")
            confirm = input(f"{YELLOW}Do you want to cancel this ticket? (yes/no): {RESET}")
            if confirm.lower() == "yes":
                self.cancel_ticket(pnr)
            else:
                print(f"{CYAN}Cancellation aborted.{RESET}")
        else:
            print(f"{RED}No ticket found for the given PNR.{RESET}")

if __name__ == "__main__":
    Cancel().run()
