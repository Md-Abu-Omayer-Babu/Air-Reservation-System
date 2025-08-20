import sqlite3

class AddCustomer:
    def __init__(self):
        self.db_path = 'airline.db'  # You can change this path as needed

    def get_input(self):
        print("ADD CUSTOMER DETAILS")
        name = input("Name: ")
        nationality = input("Nationality: ")
        aadhar = input("Aadhar Number: ")
        address = input("Address: ")
        gender = input("Gender (Male/Female): ")
        phone = input("Phone: ")
        return name, nationality, phone, address, aadhar, gender

    def save_to_db(self, name, nationality, phone, address, aadhar, gender):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS passenger (
                name TEXT, nationality TEXT, phone TEXT, address TEXT, aadhar TEXT, gender TEXT)
            ''')
            query = "INSERT INTO passenger VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (name, nationality, phone, address, aadhar, gender))
            conn.commit()
            conn.close()
            print("Customer Details Added Successfully")
        except Exception as e:
            print("Error adding customer:", e)

    def run(self):
        data = self.get_input()
        self.save_to_db(*data)

if __name__ == "__main__":
    AddCustomer().run()
