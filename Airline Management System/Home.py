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
            "7": ("Show All User Details", self.show_all_users),
            "0": ("Exit", self.exit_program)
        }
    def show_all_users(self):
        try:
            from ShowAllUsers import show_all_users
            show_all_users()
        except Exception as e:
            print("Error displaying user details:", e)

    def display_menu(self):
        # ANSI escape codes for color
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        RESET = '\033[0m'
        print(f"{CYAN}\n==============================")
        print(f"   \U0001F6EB BD AIRLINE WELCOMES YOU   ")
        print("==============================" + RESET)
        print(f"{YELLOW}Please select an option:{RESET}")
        for key, (desc, _) in self.menu_options.items():
            print(f"{GREEN}{key}. {desc}{RESET}")

    def run(self):
        BLUE = '\033[94m'
        RED = '\033[91m'
        RESET = '\033[0m'
        while True:
            self.display_menu()
            choice = input(f"{BLUE}Enter your choice: {RESET}")
            action = self.menu_options.get(choice)
            if action:
                action[1]()
            else:
                print(f"{RED}Invalid choice. Please try again.{RESET}")

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
        GREEN = '\033[92m'
        RESET = '\033[0m'
        print(f"{GREEN}Exiting program. Goodbye! \U0001F44B{RESET}")
        exit()

if __name__ == "__main__":
    Home().run()
