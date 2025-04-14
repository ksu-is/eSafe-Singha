import hashlib
import getpass

class InfoManager:
    def __init__(self):
        self.user_credentials = {}
        self.personal_info = {}

    def register_user(self, username, password):
        if username not in self.user_credentials:
            hashed_password = self._hash_password(password)
            self.user_credentials[username] = hashed_password
            self.personal_info[username] = {}
            print(f"User '{username}' registered successfully.")
        else:
            print("Username already exists. Please choose a different one.")

    def login_user(self, username, password):
        if username in self.user_credentials:
            if self._hash_password(password) == self.user_credentials[username]:
                print(f"Login successful. Welcome, {username}!")
                return True
            else:
                print("Incorrect password.")
        else:
            print("Username not found. Please register.")
        return False

    def store_info(self, username, info_type, info_data):
        if username in self.personal_info:
            self.personal_info[username][info_type] = info_data
            print(f"Personal information for '{info_type}' saved successfully.")
        else:
            print("User session not found. Please login.")

    def view_info(self, username):
        if username in self.personal_info:
            if self.personal_info[username]:
                print(f"\n Stored Personal Information for {username}:")
                for info_type, info_data in self.personal_info[username].items():
                    print(f" - {info_type}: {info_data}")
            else:
                print("No personal information stored.")
        else:
            print("User session not found. Please login.")

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

def run_info_manager():
    manager = InfoManager()
    current_user = None

    while True:
        if current_user:
            print(f"\n Logged in as: {current_user}")
            print("1. Store new personal information")
            print("2. View stored information")
            print("3. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                info_type = input("Enter the type of information (e.g. SSN, ID, Bank Info): ")
                info_data = getpass.getpass("Enter the information to store (input hidden): ")
                manager.store_info(current_user, info_type, info_data)
            elif choice == "2":
                manager.view_info(current_user)
            elif choice == "3":
                print(f"{current_user} logged out.")
                current_user = None
            else:
                print("Invalid option. Please select 1, 2, or 3.")
        else:
            print("\nPersonal Info Vault Menu")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Choose a username: ")
                password = getpass.getpass("Choose a password: ")
                manager.register_user(username, password)
            elif choice == "2":
                username = input("Enter your username: ")
                password = getpass.getpass("Enter your password: ")
                if manager.login_user(username, password):
                    current_user = username
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please enter 1, 2, or 3.")

run_info_manager()
