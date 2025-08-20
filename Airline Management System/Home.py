from Conn import Conn
import sqlite3

class Home:
    def __init__(self):
        self.menu_options = {
            "1": ("Flight Details", self.flight_details),
            "2": ("Add Customer Details", self.add_customer_details),
            "3": ("Book Flight", self.book_flight),
            "4": ("Journey Details", self.journey_details),
            "5": ("Cancel Ticket", self.cancel_ticket),
            "6": ("Boarding Pass", self.boarding_pass),
            "0": ("Exit", self.exit_program)
        }

    def display_menu(self):
        print("BD AIRLINE WELCOMES YOU")
        print("Please select an option:")
        for key, (desc, _) in self.menu_options.items():
            print(f"{key}. {desc}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            action = self.menu_options.get(choice)
            if action:
                action[1]()
            else:
                print("Invalid choice. Please try again.")

    def flight_details(self):
        from FlightInfo import FlightInfo
        FlightInfo().run()

    def add_customer_details(self):
        from AddCustomer import AddCustomer
        AddCustomer().run()

    def book_flight(self):
        from BookFlight import BookFlight
        BookFlight().run()

    def journey_details(self):
        from JourneyDetails import JourneyDetails
        JourneyDetails().run()

    def cancel_ticket(self):
        from Cancel import Cancel
        Cancel().run()

    def boarding_pass(self):
        from BoardingPass import BoardingPass
        BoardingPass().run()

    def exit_program(self):
        print("Exiting program. Goodbye!")
        exit()

if __name__ == "__main__":
    Home().run()
