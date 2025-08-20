import sqlite3

class JourneyDetails:
    def __init__(self):
        self.db_path = 'airline.db'  # Update path if needed

    def get_pnr(self):
        CYAN = '\033[96m'
        RESET = '\033[0m'
        pnr = input(f"{CYAN}Enter PNR Number: {RESET}")
        return pnr

    def show_details(self, pnr):
        CYAN = '\033[96m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        RESET = '\033[0m'
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT nid, name, src, dest, fname, fcode, date, pnr FROM tickets WHERE pnr = ?", (pnr,))
            rows = cursor.fetchall()
            if rows:
                print(f"{CYAN}\n===== JOURNEY DETAILS (Bangladesh) ====={RESET}")
                print(f"{YELLOW}NID | Name | From | To | Flight Name | Flight Code | Date | PNR{RESET}")
                for row in rows:
                    print(" | ".join(str(item) for item in row))
            else:
                print(f"{RED}No Information Found for the given PNR.{RESET}")
            conn.close()
        except Exception as e:
            print(f"{RED}Error fetching journey details: {e}{RESET}")

    def run(self):
        CYAN = '\033[96m'
        RESET = '\033[0m'
        print(f"{CYAN}\n===== JOURNEY DETAILS (Bangladesh) ====={RESET}")
        pnr = self.get_pnr()
        self.show_details(pnr)

if __name__ == "__main__":
    JourneyDetails().run()
