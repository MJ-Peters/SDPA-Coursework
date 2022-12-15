""""
SDPA Final Coursework Part A: Money Transfer System
Student: Marshall James Peters
Student ID: 2272289
"""

global_customer_data = {}  # Dictionary for storing all nested customer data
class Customer_Account:
    """
    Definiton of the Customer Account class. Data associated with each customer account is stored so that customers
    may log out and back in with their wallets and their contents still being in tact. Calling this class with all
    necessary details 'creates' the customer account. No data persistance after closing script down is needed.
    """

    def __init__(self, forename, surname, email, username, password, age, country):
        """Initialise the attributes associated with the accounts, including the users first wallet."""

        # Loops to ensure that inputs are of the correct format before storing in the dictionary
        while not forename.isalpha():
            forename = input("Sorry, your forename must contain only letters. Please try again: ")

        while not surname.isalpha():
            surname = input("Sorry, your surname must contain only letters. Please try again: ")

        while not age.isdigit():
            age = input("Sorry, your age must be a positive, whole number. Please try again: ")

        while not country.isalpha():
            country= input("Sorry, your country of residence must contain only letters. Please try again: ")


        self.forename = forename.strip()
        self.surname = surname.strip()
        self.email = email.strip()
        self.username = username.strip()
        self.password = password
        self.age = age.strip()
        self.country = country.strip()  # Country of residence of the account holder

        unique_customer_info = {}  # Dictionary for the storage of customer data (username, password etc)

        unique_customer_info["Username"] = self.username
        unique_customer_info["Password"] = self.password
        unique_customer_info["Forename"] = self.forename
        unique_customer_info["Surname"] = self.surname
        unique_customer_info["Email"] = self.email
        unique_customer_info["Age"] = self.age
        unique_customer_info["Country of Residence"] = self.country

        customer_data = {}  # Dictionary for the storage of all the customer's data

        customer_data["Customer Information"] = unique_customer_info  # Store all customer info inside customer data
        global_customer_data[self.username] = customer_data  # Link customer data with username to store in global dict

        # Creating the users first wallet so that "Associated Wallets" exists and can be added to later on.
        wallet_info = {}

        wallet_info["Wallet ID"] = f"{self.username}'s Daily Use 1"
        wallet_info["Wallet Type"] = "Daily Use"
        wallet_info["Balance"] = 0

        new_wallet = {}
        new_wallet[f"{self.username}'s Daily Use 1"] = wallet_info
        global_customer_data[self.username]["Associated Wallets"] = new_wallet

    def change_account_details(self):
        """Function to allow customers to change any of their details, except username."""

    def create_wallet(self):
        """Function to allow customers to create a wallet of specified type"""
        """Need to create wallet class first"""

    def delete_wallet(self):
        """Function to allow customers to delete a specified wallet"""
        """Need to create wallet class first"""

    def wallet_details(self):
        """Function to allow customers to see an overview of all their wallets (ID, type, and balance)"""
        """Need to create wallet class first"""

    def deposit(self):
        """Function to allow customers to deposit money to a specified wallet, daily use being the default."""
        """Need to create wallet class first"""

    def withdraw(self):
        """Function to allow customers to withdraw money from a specified walled, daily use being the default"""
        """Need to create wallet class first"""


    def transfer_wallet(self):
        """Function to allow customers to transfer money from one specified wallet to another"""
        """Need to create wallet class first"""


class Wallet:
    """
    Definition of the Wallet parent class. Customers wallet data will be stored in a dictionary with key 'Wallets'.
    This will then be stored within the customer_data dictionary, which is subsequently stored in the global dict.
    """
    def __init__(self):
        """Defining the function to display the wallets menu"""

    def create_wallet(self, username, wallet_id, wallet_type, initial_deposit):
        """Function to allow the creation of wallets"""

        wallet_info = {}
        new_wallet = {}
        self.username = username
        self.wallet_id = wallet_id
        self.wallet_type = wallet_type
        self.balance = initial_deposit


        wallet_info["Wallet ID"] = self.wallet_id
        wallet_info["Wallet Type"] = self.wallet_type
        wallet_info["Balance"] = self.balance

        global_customer_data[self.username]["Associated Wallets"][self.wallet_id] = wallet_info

    def deposit(self, username, wallet_id):
        """Definig the deposit function, which all wallet types will gain through inheritance"""

        if wallet_id in global_customer_data[username]["Associated Wallets"]:
            deposit_amount = input(f"How much money would you like to deposit into {wallet_id}? ")
            self.balance = global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"]
            self.balance += float(deposit_amount)
            global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"] = self.balance
            print("The deposit has been completed for you, returning to the menu.\n")
            return("")

        else:
            return (self.deposit(username, input("Sorry, our system did not find your wallet ID. Please try again: ")))



    def view_previous_transaction(self, wallet_id):
        """Defining the function to allow customers see the most recent transaction value and type i.e. withdraw,
        deposit, wallet/customer transfer"""

        print()


class Daily_Use(Wallet):
    """
    Definition of the Daily Use child wallet making use of inheritance for efficient design. Daily Use is the most
    flexible wallet type, having access to all possible wallet functions.
    """

    def withdraw(self, withdraw_amount):
        """Defining the function to allow customers to withdraw funds from this wallet."""

        self.balance -= withdraw_amount
        global_customer_data[self.username]["Associated Wallets"][self.wallet_id]["Balance"] = self.balance

    def wallet_transfer(self, transfer_amount, target_wallet_id):
        """Defining the function to allow customers to transfer funds from this wallet to another."""
        """
        Take into considerations the target wallet type limitations, check the type in this function. Also 0.5% fee.
        Perhaps the transfer function should call the withdraw and deposit functons inside of it.
        """
        self.transfer_amount = transfer_amount
        self.target_wallet_id = target_wallet_id


        if target_wallet_id in global_customer_data[self.username]["Associated Wallets"]:
            self.balance -= transfer_amount
            global_customer_data[self.username]["Associated Wallets"][self.wallet_id]["Balance"] = self.balance

            balance = global_customer_data[self.username]["Associated Wallets"][target_wallet_id]["Balance"]\
                      + transfer_amount
            global_customer_data[self.username]["Associated Wallets"][target_wallet_id]["Balance"] = balance

    def customer_transfer(self, transfer_amount, target_username, target_wallet_id):
        """Defining the function to allow customers to transfer funds from this wallet to another."""
        """
        Take into considerations the target wallet type limitations, check the type in this function. Also 1.5% fee.
        Perhaps the transfer function should call the withdraw and deposit functons inside of it.
        """

        if (target_username in global_customer_data)\
        and (target_wallet_id in global_customer_data[target_username]["Associated Wallets"]):

            self.balance -= transfer_amount
            global_customer_data[self.username]["Associated Wallets"][self.wallet_id]["Balance"] = self.balance

            balance = global_customer_data[target_username]["Associated Wallets"][target_wallet_id]["Balance"] \
                      + transfer_amount
            global_customer_data[target_username]["Associated Wallets"][target_wallet_id]["Balance"] = balance

        else:
            pass  # need to work out an exception for miss-inputs


class Savings(Wallet):
    """
    Definition of the Savings child wallet making use of inheritance for efficient design. Savings has restrictions on
    wallet and customer transfers.
    """
    def withdraw(self, withdraw_amount):
        """Defining the function to allow customers to withdraw funds from this wallet."""

        self.balance -= withdraw_amount
        global_customer_data[self.username]["Associated Wallets"][self.wallet_id]["Balance"] = self.balance


class Holidays(Wallet):
    """
    Definition of the Savings child wallet making use of inheritance for efficient design. Savings has restrictions on
    customer transfers.
    """
    def withdraw(self, withdraw_amount):
        """Defining the function to allow customers to withdraw funds from this wallet."""

        self.balance -= withdraw_amount
        global_customer_data[self.username]["Associated Wallets"][self.wallet_id]["Balance"] = self.balance

    def wallet_transfer(self, transfer_amount, target_wallet_id):
        """Defining the function to allow customers to transfer funds from this wallet to another"""
        """
        Take into considerations the target wallet type limitations, check the type in this function. Also 0.5% fee.
        Perhaps the transfer function should call the withdraw and deposit functons inside of it.
        """
        self.transfer_amount = transfer_amount
        self.target_wallet_id = target_wallet_id


        if target_wallet_id in global_customer_data[self.username]["Associated Wallets"]:
            self.balance -= transfer_amount
            global_customer_data[self.username]["Associated Wallets"][self.wallet_id]["Balance"] = self.balance

            balance = global_customer_data[self.username]["Associated Wallets"][target_wallet_id]["Balance"]\
                      + transfer_amount
            global_customer_data[self.username]["Associated Wallets"][target_wallet_id]["Balance"] = balance


class Mortgage(Wallet):
    """
    Definition of the Mortgage child wallet making use of inheritance for efficient design. Savings has restrictions on
    everything except deposits, it is the most restrictive wallet.
    """


class Banking_System: # TBH this is more of a customer account class, maybe change the name
    def __init__(self):
        """Initialise the attributes associated with the Banking System, including fees for transfers."""

    def log_in(self, username_input, password_input):
        """Function to allow customers to log in"""

        if (username_input in global_customer_data)\
        and (global_customer_data[username_input]["Customer Information"]["Password"] == password_input):
            print("\nYou have successfully logged in.")
            self.username = username_input
            return (self.main_menu())

        else:
            print("Your username or password was incorrect, please try again.")
            return (self.log_in(input("Please enter your username: "),
                                input("Please enter your password: ")),
                                print())

    def log_out(self):
        """Function to allow customers to log out"""

        print("You have successfully logged out, you will now be returned to the log in menu")
        print()
        return (self.login_menu())

    def login_menu(self):
        """Defining the function to display the login menu"""

        print("1) Log in to your account.")
        print("2) Create a new account.")
        print("3) Quit the money transfer system.")
        user_option = input("Please select an option, 1 through 3: ").strip()
        print()

        if user_option == "1":
            print("You have chosen to log in to your account.")
            return (self.log_in(input("Please enter your username: "),
                                input("Please enter your password: "),
                                ), print())

        elif user_option == "2":
            print("You have chosen to create a new account.")
            return (Customer_Account(input("Please enter your Forename: "),
                                     input("Please enter your Surname: "),
                                     input("Please enter your eMail: "),
                                     input("Please enter your desired username: "),
                                     input("Please enter your desired password: "),
                                     input("Please enter your age: "),
                                     input("Please enter your country of residence: ")),
                                     print(), self.login_menu())

        elif user_option == "3":
            print("Thank you for using this money transfer system, see you again next time!")
            exit()

        else:
            print("Sorry, you appear to have made an invalid selection, please try again.")
            print()
            return (self.login_menu())

    def main_menu(self):
        """Defining the function to display the main menu"""

        print("1) View wallet options.")
        print("2) View transfer options.")
        print("3) Log out of your account.")
        print("4) Delete your account.")
        user_option = input("Please select an option, 1 through 4: ").strip()
        print()

        if user_option == "1":
            print()
            print("You chose to view wallet options.")
            return (self.wallets_overview_menu())

        elif user_option == "2":
            print()
            print("You chose to view transfer options.")
            return (self.transfer_menu())

        elif user_option == "3":
            print()
            return (self.log_out())

        elif user_option == "4":
            print()
            print("You chose to delete your account.")
            return ()

        else:
            print("Sorry, you appear to have made an invalid selection, please try again.")
            print()
            return (self.main_menu())

    def wallets_overview_menu(self):
        """Defining the function to display the wallets menu"""

        print("1) Create a new wallet.")
        print("2) Deposit money to a wallet.")
        print("3) Withdraw money from a wallet.")
        print("4) View a summary of your wallets.")
        print("5) Delete a wallet.")
        print("6) Return to the previous menu.")
        user_option = input("Please select an option, 1 through 6: ").strip()
        print()

        if user_option == "1":
            return (self.create_wallets_menu())

        elif user_option == "2":
            return(Wallet().deposit(self.username,
                                    input("What is the ID of the wallet you'd like to deposit to? ").strip()))


        elif user_option == "3":
            return ()

        elif user_option == "4":
            return (self.wallets_summary())

        elif user_option == "5":
            return ()

        elif user_option == "6":
            print()
            print("You chose to return to the main menu.")
            return (self.main_menu())

        else:
            print("Sorry, you appear to have made an invalid selection, please try again.")
            print()
            return (self.wallets_overview_menu())

    def create_wallets_menu(self):
        """Defining the function to interact with the wallets classes to create new instances"""

        print("You chose to create a wallet.")
        print("1) Daily Use.")
        print("2) Savings.")
        print("3) Holidays.")
        print("4) Mortgage.")
        print("5) Return to the previous menu")
        user_option = input("Please select an option, 1 through 5: ").strip()
        print()

        if user_option == "1":
            wallet_id = input("Please enter the ID (name) you'd like to assign your Daily Use wallet: ").strip()
            wallet_type = "Daily Use"
            initial_deposit = input("Please enter how much money you'd like to deposit: ").strip()
            return (Daily_Use().create_wallet(self.username, wallet_id, wallet_type, float(initial_deposit)),
                    self.create_wallets_menu())

        elif user_option == "2":
            wallet_id = input("Please enter the ID (name) you'd like to assign your Savings wallet: ").strip()
            wallet_type = "Savings"
            initial_deposit = input("Please enter how much money you'd like to deposit: ").strip()
            return (Savings().create_wallet(self.username, wallet_id, wallet_type, float(initial_deposit)),
                    self.create_wallets_menu())

        elif user_option == "3":
            wallet_id = input("Please enter the ID (name) you'd like to assign your Holidays wallet: ").strip()
            wallet_type = "Holidays"
            initial_deposit = input("Please enter how much money you'd like to deposit: ").strip()
            return (Holidays().create_wallet(self.username, wallet_id, wallet_type, float(initial_deposit)),
                    self.create_wallets_menu())

        elif user_option == "4":
            wallet_id = input("Please enter the ID (name) you'd like to assign your Mortgage wallet: ").strip()
            wallet_type = "Mortgage"
            initial_deposit = input("Please enter how much money you'd like to deposit: ").strip()
            return (Mortgage().create_wallet(self.username, wallet_id, wallet_type, float(initial_deposit)),
                    self.create_wallets_menu())

        elif user_option == "5":
            print()
            print("You chose to return to view wallet options.")
            return (self.wallets_overview_menu())

        else:
            print("Sorry, you appear to have made an invalid selection, please try again.")
            print()
            return (self.create_wallets_menu())

    def wallets_summary(self):
        """"""

        for key, value in global_customer_data[self.username]["Associated Wallets"].items():
            wallet_type = value["Wallet Type"]
            balance = value["Balance"]

            print(f"{key}:")
            print(f"Type: {wallet_type}")
            print(f"Balance: £{balance}")
            print()

        print("A summary of all your wallets can be seen above, returning to the menu.")
        return(self.wallets_overview_menu())

    def transfer_menu(self):
        """Defining function to display the transfer menu"""

        print("You chose to view transfer options")
        print("1) Transfer money between your wallets.")
        print("2) Transfer money to another customer.")
        print("3) Return to the previous menu")
        user_option = input("Please select an option, 1 through 3: ").strip()
        print()

        if user_option == "1":
            return ()

        elif user_option == "2":
            return ()

        elif user_option == "3":
            print()
            print("You chose to return to the main menu.")
            return (self.main_menu())

        else:
            print("Sorry, you appear to have made an invalid selection, please try again.")
            print()
            return (self.transfer_menu())



Banking_System().login_menu()
print(global_customer_data["m"]["Associated Wallets"])
