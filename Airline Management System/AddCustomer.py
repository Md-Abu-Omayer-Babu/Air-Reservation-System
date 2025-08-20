import sqlite3

class AddCustomer:
    def __init__(self):
        self.db_path = 'airline.db'  # You can change this path as needed

    def get_input(self):
        CYAN = '\033[96m'
        YELLOW = '\033[93m'
        RESET = '\033[0m'
        print(f"{CYAN}\n===== ADD CUSTOMER DETAILS (Bangladesh) ====={RESET}")
        name = input(f"{YELLOW}Full Name: {RESET}")
        nationality = 'Bangladeshi'
        nid = input(f"{YELLOW}NID Number: {RESET}")
        address = input(f"{YELLOW}Address (District, Upazila): {RESET}")
        gender = input(f"{YELLOW}Gender (Male/Female/Other): {RESET}")
        phone = input(f"{YELLOW}Mobile Number (+880): {RESET}")
        return name, nationality, phone, address, nid, gender

    def save_to_db(self, name, nationality, phone, address, nid, gender):
        GREEN = '\033[92m'
        RED = '\033[91m'
        RESET = '\033[0m'
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS passenger (
                name TEXT, nationality TEXT, phone TEXT, address TEXT, nid TEXT, gender TEXT)
            ''')
            query = "INSERT INTO passenger VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (name, nationality, phone, address, nid, gender))
            conn.commit()
            conn.close()
            print(f"{GREEN}\u2714 Customer Details Added Successfully!{RESET}")
        except Exception as e:
            print(f"{RED}Error adding customer: {e}{RESET}")

    def run(self):
        data = self.get_input()
        self.save_to_db(*data)

if __name__ == "__main__":
    AddCustomer().run()
