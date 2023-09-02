class Passenger:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class BusPass:
    def __init__(self, pass_type, price):
        self.pass_type = pass_type
        self.price = price

class BusBookingSystem:
    def __init__(self):
        self.passengers = []
        self.bus_passes = []
        self.logged_in_user = None

    def register_passenger(self, username, password):
        passenger = Passenger(username, password)
        self.passengers.append(passenger)
        print(f"User {username} registered successfully.")

    def login(self, username, password):
        for passenger in self.passengers:
            if passenger.username == username and passenger.password == password:
                self.logged_in_user = passenger
                print(f"Welcome, {username}!")
                return
        print("Invalid username or password. Please try again.")

    def purchase_bus_pass(self, pass_type):
        if self.logged_in_user:
            for bus_pass in self.bus_passes:
                if bus_pass.pass_type == pass_type:
                    print(f"Bus pass ({pass_type}) purchased for ${bus_pass.price}")
                    return
            print(f"Bus pass ({pass_type}) not found.")
        else:
            print("Please log in first.")

    def add_bus_pass(self, pass_type, price):
        bus_pass = BusPass(pass_type, price)
        self.bus_passes.append(bus_pass)
        print(f"Bus pass ({pass_type}) added to the system.")

if __name__ == "__main__":
    bus_system = BusBookingSystem()

    while True:
        print("\nMenu:")
        print("1. Register Passenger")
        print("2. Login")
        print("3. Add Bus Pass")
        print("4. Purchase Bus Pass")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            bus_system.register_passenger(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            bus_system.login(username, password)
        elif choice == "3":
            if bus_system.logged_in_user:
                pass_type = input("Enter pass type: ")
                price = float(input("Enter price: "))
                bus_system.add_bus_pass(pass_type, price)
            else:
                print("Please log in first.")
        elif choice == "4":
            if bus_system.logged_in_user:
                pass_type = input("Enter pass type: ")
                bus_system.purchase_bus_pass(pass_type)
            else:
                print("Please log in first.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
