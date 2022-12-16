""""
SDPA Final Coursework Part A: Money Transfer System
Student: Marshall James Peters
Student ID: 2272289
"""
import re

global_customer_data = {}  # Dictionary for storing all nested customer data

class Customer_Account:
    """
    Definiton of the Customer Account class. Data associated with each customer account is stored so that customers
    may log out and back in with their wallets and their contents still being in tact. Calling this class with all
    necessary details 'creates' the customer account. No data persistance after closing script down is needed.
    """

    def __init__(self):
        """Initialise the attributes associated with the accounts, including the users first wallet."""

    def login_menu(self):
        """Defining the function to display the login menu"""

        print("1) Log in to your account.")
        print("2) Create a new account.")
        print("3) Quit the money transfer system.")
        user_option = input("Please select an option, 1 through 3: ").strip()
        print()

        if user_option == "1":
            return (self.log_in(input("Please enter your username: "),
                                input("Please enter your password: "),
                                ), print())

        elif user_option == "2":
            return (self.create_account(input("Please enter your Forename: "),
                                        input("Please enter your Surname: "),
                                        input("Please enter your eMail: "),
                                        input("Please enter your desired username (minimum length 5): "),
                                        input("Please enter your desired password (minimum length 8): "),
                                        input("Please enter your age: "),
                                        input("Please enter your country of residence: ")),
                                        self.login_menu())

        elif user_option == "3":
            print("Thank you for using this money transfer system, see you again next time!")
            exit()

        else:
            print("Sorry, you appear to have made an invalid selection, please try again.")
            print()
            return (self.login_menu())

    def create_account(self, forename, surname, email, username, password, age, country):
        """Defining the function"""

        # Loops to ensure that inputs are of the correct format before storing in the dictionary
        while not (forename.isalpha() and len(forename) >= 1) :
            forename = input("Your forename must contain only letters and be of minimum length 1. Please try again: ").strip()

        while not (surname.isalpha() and len(surname) >= 1):
            surname = input("Your surname must contain only letters and be of minimum length 1. Please try again: ").strip()

        # ^@ checks that the string within [^@] is not an '@'. The below re.match basically checks that the email is in
        # the format "string" + @"string" + ."string"
        while not re.match("[^@]+@[^@]+\.[^@]+", email):
            email = input("Please enter a valid email address: ").strip()

        while not len(username) >= 5:
            username = input("Your username must be at least 5 characters. Please try again: ").strip()

        while username in global_customer_data:
            username = input("Sorry, that username is taken. Please try again: ").strip()

        while not len(password) >= 8:
            password = input("Your password must be at least 8 characters. Please try again: ").strip()

        while not age.isdigit():
            age = input("Your age must be a positive, whole number. Please try again: ").strip()

        while not (country.isalpha() or len(country) > 1):  # Country of residence of the account holder
            country= input("Your country of residence must contain only letters. Please try again: ").strip()

        unique_customer_info = {}  # Dictionary for the storage of customer data (username, password etc)

        unique_customer_info["Username"] = username
        unique_customer_info["Password"] = password
        unique_customer_info["Forename"] = forename
        unique_customer_info["Surname"] = surname
        unique_customer_info["Email"] = email
        unique_customer_info["Age"] = age
        unique_customer_info["Country of Residence"] = country

        customer_data = {}  # Dictionary for the storage of all the customer's data

        customer_data["Customer Information"] = unique_customer_info  # Store all customer info inside customer data
        global_customer_data[username] = customer_data  # Link customer data with username to store in global dict

        # Creating the users first wallet so that "Associated Wallets" exists and can be added to later on.
        wallet_info = {}

        wallet_info["Wallet ID"] = f"{username}'s Daily Use 1"
        wallet_info["Wallet Type"] = "Daily Use"
        wallet_info["Balance"] = 0

        new_wallet = {}
        new_wallet[f"{username}'s Daily Use 1"] = wallet_info
        global_customer_data[username]["Associated Wallets"] = new_wallet

        print("\nAccount successfully created. A Daily Use wallet, " +
              f"with ID '{username}'s Daily Use 1', has been created for you.")

    def log_in(self, username_input, password_input):
        """Function to allow customers to log in"""

        if (username_input in global_customer_data) \
                and (global_customer_data[username_input]["Customer Information"]["Password"] == password_input):
            print("\nYou have successfully logged in.")
            username = username_input
            return (Banking_System(username).main_menu())

        else:
            print("\nYour username or password was incorrect, please try again.")
            return (self.log_in(input("Please enter your username: "),
                                input("Please enter your password: ")),
                    print())

    def log_out(self, username):
        """Function to allow customers to log out"""

        print("You have successfully logged out, you will now be returned to the log in menu")
        print()
        return (self.login_menu())

    def change_account_details(self, username):
        """Function to allow customers to change any of their details, except username."""
        print("")

    def delete_account(self, username):
        """Function that will allow a customer to delete their whole account from the system."""

        global_customer_data.pop(username)
        print(f"\nYour account (username: {username}) has been deleted, returning to the login menu.")
        return (self.login_menu())

    def create_wallet(self, username, user_option):
        """Function to allow customers to create a wallet of specified type"""

        if user_option == "1":
            wallet_id = input("Please enter the ID (name) you'd like to assign your Daily Use wallet: ").strip()
            wallet_type = "Daily Use"
            initial_deposit = input("Please enter how much money you'd like to deposit: ").strip()
            return (Daily_Use().create_wallet(username, wallet_id, wallet_type, float(initial_deposit)),
                    Banking_System(username).create_wallets_menu())

        elif user_option == "2":
            wallet_id = input("Please enter the ID (name) you'd like to assign your Savings wallet: ").strip()
            wallet_type = "Savings"
            initial_deposit = input("Please enter how much money you'd like to deposit: ").strip()
            return (Savings().create_wallet(username, wallet_id, wallet_type, float(initial_deposit)),
                    Banking_System(username).create_wallets_menu())

        elif user_option == "3":
            wallet_id = input("Please enter the ID (name) you'd like to assign your Holidays wallet: ").strip()
            wallet_type = "Holidays"
            initial_deposit = input("Please enter how much money you'd like to deposit: ").strip()
            return (Holidays().create_wallet(self.username, wallet_id, wallet_type, float(initial_deposit)),
                    Banking_System(username).create_wallets_menu())

        elif user_option == "4":
            wallet_id = input("Please enter the ID (name) you'd like to assign your Mortgage wallet: ").strip()
            wallet_type = "Mortgage"
            initial_deposit = input("Please enter how much money you'd like to deposit: ").strip()
            return (Mortgage().create_wallet(self.username, wallet_id, wallet_type, float(initial_deposit)),
                    Banking_System(username).create_wallets_menu())

        elif user_option == "5":
            print()
            print("You chose to return to view wallet options.")
            return (Banking_System(username).wallets_overview_menu())

        else:
            print("Sorry, you appear to have made an invalid selection, please try again.")
            print()
            return (Banking_System(username).create_wallets_menu())

    def delete_wallet(self, username, wallet_id):
        """Function to allow customers to delete a specified wallet"""
        if wallet_id in global_customer_data[username]["Associated Wallets"]:
            if global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"] != 0:
                double_check = input("Are you sure you want to delete your wallet? Move any remaining funds if the " +
                                     "the wallet is of a type that allows you to do so or they will be lost. " +
                                     "Please enter yes or no: ").lower()

            else:
                double_check = input("Are you sure you want to delete your wallet? " +
                                     "Please enter yes or no: ").lower()

            if double_check == "yes":
                password_check = input("Please enter your password to confirm this action. Incorrect password will " +
                                       "take you back to the previous menu: ")

                if password_check == global_customer_data[username]["Customer Information"]["Password"]:
                    return (Wallet().delete_wallet(username, wallet_id),
                            Banking_System(username).wallets_overview_menu())

                else:
                    print("\nPassword incorrect, returning to the previous menu")
                    return(Banking_System(username).wallets_overview_menu())

            elif double_check == "no":
                print("\nWallet deletion cancelled, returning to the previous menu.")
                return (Banking_System(username).wallets_overview_menu())

            else:
                print("Invalid response.")
                return (self.delete_wallet(username, wallet_id))

        else:
            print("Wallet ID not found, returning to the previous menu.")
            return (Banking_System(username).wallets_overview_menu())

    def wallets_summary(self, username):
        """Function to give a summary of all wallets held by an account."""

        if len(global_customer_data[username]["Associated Wallets"].items()) != 0:

            for key, value in global_customer_data[username]["Associated Wallets"].items():
                wallet_type = value["Wallet Type"]
                balance = round(value["Balance"], 2)

                print(f"{key}:")
                print(f"Type: {wallet_type}")
                print("Balance: £{:,.2f}".format(balance))  # Makes the number a nice readable format with commas every 000
                print()

            print("A summary of all your wallets can be seen above, returning to the previous menu.")

        else:
            print("You do not have any wallets to display, returning to the previous menu.")

        return (Banking_System(username).wallets_overview_menu())

    def deposit(self, username, wallet_id):
        """Function to allow customers to deposit money to a specified wallet, daily use being the default."""

        if wallet_id in global_customer_data[username]["Associated Wallets"]:
            return (Wallet().deposit(username, wallet_id))

        else:
            return (self.deposit(username, input("Your wallet ID could not be found, please try again: ")))

    def withdraw(self, username, wallet_id):
        """Function to allow customers to withdraw money from a specified walled, daily use being the default"""

        if wallet_id in global_customer_data[username]["Associated Wallets"]:
            wallet_type = global_customer_data[username]["Associated Wallets"][wallet_id]["Wallet Type"]

            if wallet_type == "Daily Use":
                return (Daily_Use().withdraw(username, wallet_id))

            elif wallet_type == "Savings":
                return (Savings().withdraw(username, wallet_id))

            elif wallet_type == "Holidays":
                return (Holidays().withdraw(username, wallet_id))

            elif wallet_type == "Mortgage":
                return (Mortgage().withdraw(username, wallet_id))

            else:
                print("An error has occurred, please try again later.")
                return (Banking_System(username).wallets_overview_menu())

    def wallet_transfer(self, username, wallet_id):
        """Function to allow customers to transfer money from one specified wallet to another"""

        if wallet_id in global_customer_data[username]["Associated Wallets"]:
            wallet_type = global_customer_data[username]["Associated Wallets"][wallet_id]["Wallet Type"]

            if wallet_type == "Daily Use":
                return (Daily_Use().wallet_transfer(username, wallet_id))

            elif wallet_type == "Savings":
                return (Savings().wallet_transfer(username, wallet_id))

            elif wallet_type == "Holidays":
                return (Holidays().wallet_transfer(username, wallet_id))

            elif wallet_type == "Mortgage":
                return (Mortgage().wallet_transfer(username, wallet_id))

            else:
                print("An error has occurred, please try again later.")
                return (Banking_System(username).transfer_menu())

    def customer_transfer(self, username, wallet_id, target_username, target_wallet_id):
        """Function to allow customers to transfer money from a specified wallet to another user."""

        if wallet_id in global_customer_data[username]["Associated Wallets"]:
            wallet_type = global_customer_data[username]["Associated Wallets"][wallet_id]["Wallet Type"]

            if wallet_type == "Daily Use":
                return (Daily_Use().customer_transfer(username, wallet_id, target_username, target_wallet_id))

            elif wallet_type == "Savings":
                return (Savings().customer_transfer(username, wallet_id, target_username, target_wallet_id))

            elif wallet_type == "Holidays":
                return (Holidays().customer_transfer(username, wallet_id, target_username, target_wallet_id))

            elif wallet_type == "Mortgage":
                return (Mortgage().customer_transfer(username, wallet_id, target_username, target_wallet_id))

            else:
                print("An error has occurred, please try again later.")
                return (Banking_System(username).transfer_menu())
        # Password confirmation to make sure customer wants to transfer the money to someone else.

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
        print("\nYour wallet has been successfully created, returning to the previous menu.")

    def deposit(self, username, wallet_id):
        """Defining the function to allow customers to deposit funds to their wallet."""

        deposit_amount = input(f"How much money would you like to deposit into {wallet_id}? ")
        balance = global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"]
        balance += float(deposit_amount)
        global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"] = balance
        print("\nThe deposit has been completed for you, returning to the previous menu.")

        return (Banking_System(username).wallets_overview_menu())

    def withdraw(self, username, wallet_id):
        """Defining the function to allow customers to withdraw funds from their wallet. This function will
        be overwritten if the child wallet is not allowedd to execute on the coursework brief."""

        withdraw_amount = input(f"How much money would you like to withdraw from {wallet_id}? ")
        balance = global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"]
        balance -= float(withdraw_amount)
        global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"] = balance
        print("\nThe withdrawal has been completed for you, returning to the previous menu.")

        return (Banking_System(username).wallets_overview_menu())

    def wallet_transfer(self, username, wallet_id):
        """Defining the function to allow customers to transfer funds from this wallet to another. This function will
        be overwritten if the child wallet is not allowedd to execute on the coursework brief."""

        target_wallet_id = input("Please enter the ID of the wallet you would like to transfer to: ")
        target_wallet_type = global_customer_data[username]["Associated Wallets"][target_wallet_id]["Wallet Type"]
        transfer_amount = input("Please enter money you would like to transfer " +
                                f"to {target_wallet_id} from {wallet_id}: ")

        # This check of the target is only important when the wallet executing the transfer is allowed to,
        # otherwise this whole function will be overwritten to reject the transaction before the check occurs.
        if target_wallet_type == "Daily Use":
            pass  # Daily use can recieve transfers

        elif target_wallet_type == "Savings":
            print("\nSavings wallets are unable to recieve transfers, returning to the previous menu.")
            return (Banking_System(username).transfer_menu())

        elif target_wallet_type == "Holidays":
            pass  # Holidays can recieve transfers

        elif target_wallet_type == "Mortgage":
            print("\nMortgage wallets are unable to recieve transfers, returning to the previous menu.")
            return (Banking_System(username).transfer_menu())

        else:
            print("\nAn error has occurred, please try again later.")
            return (Banking_System(username).transfer_menu())


        balance = global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"]
        balance -= float(transfer_amount)
        global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"] = balance

        target_balance = global_customer_data[username]["Associated Wallets"][target_wallet_id]["Balance"]
        target_balance += float(transfer_amount)
        global_customer_data[username]["Associated Wallets"][target_wallet_id]["Balance"] = target_balance

        print("\nThe wallet transfer has been completed for you, returning to the previous menu.")
        return(Banking_System(username).transfer_menu())

    # NEEDS FIXING
    def customer_transfer(self, username, wallet_id, target_username, target_wallet_id):
        """Defining the function to allow customers to transfer funds from this wallet to another. This function will
        be overwritten if the child wallet is not allowedd to execute on the coursework brief."""

        if (target_username in global_customer_data)\
        and (target_wallet_id in global_customer_data[target_username]["Associated Wallets"]):
            transfer_amount = float(input(f"Enter the amount you would like to transfer to {target_username}: "))

            if transfer_amount <=0:
                print("\nYou cannot transfer a negative or null amount of money")
                return (self.customer_transfer(username, wallet_id, target_username, target_wallet_id))

            else:
                donor_balance = global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"]
                donor_balance -= transfer_amount  # later needs inclusion of fee
                global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"] = donor_balance

                target_balance = global_customer_data[target_username]["Associated Wallets"]\
                                                     [target_wallet_id]["Balance"]
                target_balance += transfer_amount
                global_customer_data[target_username]["Associated Wallets"]\
                                    [target_wallet_id]["Balance"] = target_balance
                print(f"\nTransfer to {target_username} complete, returning to the previous menu.")
                return (Banking_System(username).transfer_menu())

        else:
            if not target_username in global_customer_data:
                print("\nThe user you have specified does not exist, returning to the previous menu.")
                return (Banking_System(username).transfer_menu())

            elif not target_wallet_id in global_customer_data[target_username]["Associated Wallets"]:
                print("\nThe user does not have a wallet with the ID you specified, returning to the previous menu.")
                return (Banking_System(username).transfer_menu())

    # NEEDS MAKING
    def view_previous_transaction(self, wallet_id):
        """Defining the function to allow customers see the most recent transaction value and type i.e. withdraw,
        deposit, wallet/customer transfer"""

        return ()

    def delete_wallet(self, username, wallet_id):
        """Definition of the function to delete a user's wallet, if it exists."""

        global_customer_data[username]["Associated Wallets"].pop(wallet_id, None)  # sets the default to None
        print(f"\nIf you had a wallet with ID '{wallet_id}' it was deleted, returning to the previous menu")
        return (Banking_System(username).wallets_overview_menu())

class Daily_Use(Wallet):
    """
    Definition of the Daily Use child wallet making use of inheritance for efficient design. Daily Use is the most
    flexible wallet type, having access to all possible wallet functions.
    """
    pass  # All methods are inherited, no exceptions need to be raised

class Savings(Wallet):
    """
    Definition of the Savings child wallet making use of inheritance for efficient design. Savings has restrictions on
    wallet and customer transfers.
    """
    def wallet_transfer(self, username, wallet_id):
        print("Savings wallets are unable to send or recieve wallet transfers, returning to the previous menu.")
        return (Banking_System(username).wallets_overview_menu())

    def customer_transfer(self, username, wallet_id):
        print("Savings wallets are unable to send or recieve customer transfers, returning to the previous menu.")
        return (Banking_System(username).wallets_overview_menu())

class Holidays(Wallet):
    """
    Definition of the Savings child wallet making use of inheritance for efficient design. Savings has restrictions on
    customer transfers.
    """
    def customer_transfer(self, username, wallet_id):
        print("Holidays wallets are unable to send or recieve customer transfers, returning to the previous menu.")
        return (Banking_System(username).wallets_overview_menu())

class Mortgage(Wallet):
    """
    Definition of the Mortgage child wallet making use of inheritance for efficient design. Savings has restrictions on
    everything except deposits, it is the most restrictive wallet.
    """
    def withdraw(self, username, wallet_id):
        print("\nMortgage wallets are unable withdraw, returning to the previous menu.")
        return (Banking_System(username).wallets_overview_menu())
    def wallet_transfer(self, username, wallet_id):
        print("\nMortgage wallets are unable to send or recieve wallet transfers, returning to the previous menu.")
        return (Banking_System(username).transfer_menu())

    def customer_transfer(self, username, wallet_id):
        print("\nMortgage wallets are unable to send or recieve customer transfers, returning to the previous menu.")
        return (Banking_System(username).wallets_overview_menu())

class Banking_System: # TBH this is more of a customer account class, maybe change the name
    def __init__(self, username):
        """Initialise the attributes associated with the Banking System, including fees for transfers."""

        self.username = username
        self.password = global_customer_data[self.username]["Customer Information"]["Password"]

    def main_menu(self):
        """Defining the function to display the main menu"""

        print("1) View wallet options.")
        print("2) View transfer options.")
        print("3) Log out of your account.")
        print("4) Delete your account.")
        user_option = input("Please select an option, 1 through 4: ").strip()

        if user_option == "1":
            print("\nYou chose to view wallet options.")
            return (self.wallets_overview_menu())

        elif user_option == "2":
            print("\nYou chose to view transfer options.")
            return (self.transfer_menu())

        elif user_option == "3":
            print()
            return (Customer_Account().log_out(self.username))

        elif user_option == "4":
            print("\nYou have chosen to delete your account. You will lose all money in any wallets you have left.")
            double_check = input("Are you sure you wish to proceed? Please enter yes or no: ").lower()

            if double_check == "yes":
                password_check = input("Please enter your password to confirm your acknowledgment " +
                                       "of the previous statement: ")

                if password_check == self.password:
                    return (Customer_Account().delete_account(self.username))

                else:
                    print("Password incorrect, returning to the previous menu.")
                    return (self.main_menu())

        else:
            print("Sorry, you appear to have made an invalid selection, please try again.\n")
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
            return(Customer_Account().deposit(self.username,
                   input("What is the ID of the wallet you'd like to deposit to? ").strip()))

        elif user_option == "3":

            return (Customer_Account().withdraw(self.username,
                    input("What is the ID of the wallet you'd like to withdraw from? ").strip()))

        elif user_option == "4":
            return (Customer_Account().wallets_summary(self.username))

        elif user_option == "5":
            return (Customer_Account().delete_wallet(self.username,
                    input("Please enter the ID of the wallet you would like to delete: ").strip()))

        elif user_option == "6":
            print("\nYou chose to return to the main menu.")
            return (self.main_menu())

        else:
            print("\nSorry, you appear to have made an invalid selection, please try again.")
            return (self.wallets_overview_menu())

    def create_wallets_menu(self):
        """Defining the function to interact with the wallets classes to create new instances"""

        print("1) Daily Use.")
        print("2) Savings.")
        print("3) Holidays.")
        print("4) Mortgage.")
        print("5) Return to the previous menu")
        user_option = input("Please select an option, 1 through 5: ").strip()

        return (Customer_Account().create_wallet(self.username, user_option))

    def transfer_menu(self):
        """Defining function to display the transfer menu"""

        print("1) Transfer money between your wallets.")
        print("2) Transfer money to another customer.")
        print("3) Return to the previous menu")
        user_option = input("Please select an option, 1 through 3: ").strip()

        """ADD A PASSWORD CHECK FOR CUSTOMER TRANSFERS."""
        if user_option == "1":
            return (Customer_Account().wallet_transfer(self.username,
                    input("\nPlease enter the ID of the wallet you would like to transfer from: ")))

        elif user_option == "2":
            return (Customer_Account().customer_transfer(self.username,
                    input("\nPlease enter the ID of the wallet you would like to transfer from: "),
                    input("Please enter the username of the customer you would like to transfer to: "),
                    input("Please enter the ID of the target wallet belonging to the specified customer: ")))

        elif user_option == "3":
            print("\nYou chose to return to the main menu.")
            return (self.main_menu())

        else:
            print("\nSorry, you appear to have made an invalid selection, please try again.")
            return (self.transfer_menu())


Customer_Account().login_menu()


