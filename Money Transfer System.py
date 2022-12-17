""""
SDPA Final Coursework Part A: Money Transfer System
Student: Marshall James Peters
Student ID: 2272289
"""
import re  # Standard library package used for string format testing (i.e. checking valid email addresses)
import csv  # Standard library package used for csv operations (needed for the bonus task)

# Starting the script with the global data store with a Bank account defined to store transfer fees
global_customer_data = {"Bank": {"Customer Information": {"Username": "Bank", "Password": "ADMIN", "Forename": "N/A",
                                                          "Surname": "N/A", "Email": "bank@bank.com", "Age": "N/A",
                                                          "Country of Residence": "UK"},
                                 "Associated Wallets": {"Fee Tracker": {"Wallet ID": "Fee Tracker",
                                                                        "Wallet Type": "Bank",
                                                                        "Balance": 0}}}}

class Customer_Account:
    """
    Definiton of the Customer Account class. Data associated with each customer account is stored so that customers
    may log out and back in with their wallets and their contents still being in tact.
    """

    def __init__(self):
        """No initialised attributes were needed for this class."""
        pass

    def login_menu(self):
        """Function to display the login menu and enable interaction with it."""

        print("1) Log in to your account.")
        print("2) Create a new account.")
        print("3) Quit the money transfer system.")
        user_option = input("Please select the option corresponding to your choice: ").strip()

        if user_option == "1":  # Sends user to the log in method
            return (self.log_in(input("\nPlease enter your username: "),
                                input("Please enter your password: "),
                                ), print())

        elif user_option == "2":  # sends user to the create account method
            return (self.create_account(input("\nPlease enter your Forename: "),
                                        input("Please enter your Surname: "),
                                        input("Please enter your eMail: "),
                                        input("Please enter your desired username (minimum length 5): "),
                                        input("Please enter your desired password (minimum length 8): "),
                                        input("Please enter your age: "),
                                        input("Please enter your country of residence: ")),
                                        self.login_menu())

        elif user_option == "3":  # Exiting the program for the user.
            print("Thank you for using this money transfer system, see you again next time!")
            exit()

        else:  # Error handling for any bad inputs
            print("Sorry, you appear to have made an invalid selection, please try again.")
            print()
            return (self.login_menu())

    def create_account(self, forename, surname, email, username, password, age, country):
        """
        Function to allow customers to create an account. The function performs checks to ensure that all
        inputs are of the right format and, in the case of username, are not already in existance.
        """

        while not (forename.isalpha() and len(forename) >= 1) :  # Checking forename is in ok format
            forename = input("Your forename must contain only letters and be of minimum length 1. " +
                             "Please try again: ").strip()

        while not (surname.isalpha() and len(surname) >= 1):  # Checking surname is in ok format
            surname = input("Your surname must contain only letters and be of minimum length 1. " +
                            "Please try again: ").strip()

        # ^@ checks that the string within [^@] is not an '@'. The below re.match basically checks that the email is in
        # the format "string" + @"string" + ."string"
        while not re.match("[^@]+@[^@]+\.[^@]+", email):  # Checking email is in ok format
            email = input("Please enter a valid email address: ").strip()

        while not len(username) >= 5:  # Checking username has a suitable length
            username = input("Your username must be at least 5 characters. Please try again: ").strip()

        while username in global_customer_data:  # Checking the availability of the username
            username = input("Sorry, that username is taken. Please try again: ").strip()

        while not len(password) >= 8:  # Checking password has a suitable length
            password = input("Your password must be at least 8 characters. Please try again: ").strip()

        while not age.isdigit():  # Checking age is a positive integer
            age = input("Your age must be a positive, whole number. Please try again: ").strip()

        while not (country.isalpha() and len(country) >= 1):  # Checking Country of residence is in ok format
            country= input("Your country of residence must contain only letters. Please try again: ").strip()

        unique_customer_info = {}  # Dictionary for the storage of customer info (username, password etc)

        unique_customer_info["Username"] = username
        unique_customer_info["Password"] = password
        unique_customer_info["Forename"] = forename
        unique_customer_info["Surname"] = surname
        unique_customer_info["Email"] = email
        unique_customer_info["Age"] = age
        unique_customer_info["Country of Residence"] = country

        customer_data = {}  # Dictionary for the storage of all the customer's data (info, wallets etc)

        customer_data["Customer Information"] = unique_customer_info  # Store all customer info inside customer data
        global_customer_data[username] = customer_data  # Link customer data with username to store in global dict

        # Creating the users first wallet so that "Associated Wallets" exists and can be added to later on.
        wallet_info = {}
        transaction_info = {}  # Dictionary for the storage of data on the most recent transaction for that wallet

        wallet_info["Wallet ID"] = f"{username}'s Daily Use 1"  # Defining first wallet generic name based on username
        wallet_info["Wallet Type"] = "Daily Use"  # Defining the wallet type
        wallet_info["Balance"] = 0  # Defining the wallet balance
        transaction_info["Transaction Type"] = "None"  # Defining the type of previous transaction
        transaction_info["Transaction Value"] = 0  # Defining the value of that transaction
        wallet_info["Previous Transaction"] = transaction_info  # Storing that transaction info in the main dict

        new_wallet = {}  # Dict to hold all info on the users first wallet
        new_wallet[f"{username}'s Daily Use 1"] = wallet_info  # Adding the wallet info and linking to the wallet ID
        global_customer_data[username]["Associated Wallets"] = new_wallet  # Adding the linked wallet to the global dict

        self.write_to_csv(username, password)  # Calling the csv function to write the initial user/pword to the csv

        print("\nAccount successfully created. A Daily Use wallet, " +
              f"with ID '{username}'s Daily Use 1', has been created for you.")  # Announcing that the creation is done

    def log_in(self, username_input, password_input):
        """Function to allow customers to log in and access methods to do with their account and wallets."""

        # Checking that the login info matches what is stored in the global dict
        if (username_input in global_customer_data) \
                and (global_customer_data[username_input]["Customer Information"]["Password"] == password_input):
            print("\nYou have successfully logged in.")
            username = username_input
            return (Banking_System(username).main_menu())  # Giving access to system if details are correct

        else:
            print("\nYour username or password was incorrect, please try again.")
            return (self.log_in(input("Please enter your username: "),
                                input("Please enter your password: ")),  # Prompting new entry if details were incorrect
                    print())

    def log_out(self, username):
        """Function to allow customers to log out of their account, revoking access to account details etc"""

        print("You have successfully logged out, you will now be returned to the log in menu\n")
        return (self.login_menu())  # Returning to the log in menu to make customers sign back in for access

    def change_account_details(self, username, user_option):
        """
        Function to allow customers to change any of their account details. Inputs are recieved from the Banking
        System class that contains all internal (beyond login) menu interactions.
        """

        if user_option == "1":  # Triggers the change in forename
            new_forename = input("\nPlease enter your new forename: ").strip()
            while not (new_forename.isalpha() and len(new_forename) >= 1):  # Checking forename is in ok format
                forename = input("Your forename must contain only letters and be of minimum length 1. " +
                                 "Please try again: ").strip()

            global_customer_data[username]["Customer Information"]["Forename"] = new_forename  # Updating global dict
            print("Your forename has been changed successfully, returning to the previous menu.")
            return (Banking_System(username).change_details_menu())  # Returning to the menu they were last on

        elif user_option == "2":  # Triggers the change in surname
            new_surname = input("Please enter your new surname: ").strip()
            while not (new_surname.isalpha() and len(new_surname) >= 1):  # Checking surname is in ok format
                surname = input("Your surname must contain only letters and be of minimum length 1. " +
                                "Please try again: ").strip()

            global_customer_data[username]["Customer Information"]["Surname"] = new_surname  # Updating global dict
            print("\nYour surname has been changed successfully, returning to the previous menu.")
            return (Banking_System(username).change_details_menu())  # Returning to the menu they were last on

        elif user_option == "3": # Triggers the change in email address
            new_email = input("Please enter your new email address: ").strip()
            while not re.match("[^@]+@[^@]+\.[^@]+", new_email):  # Checking email is in ok format
                new_email = input("Please enter a valid email address: ").strip()

            global_customer_data[username]["Customer Information"]["Email"] = new_email  # Updating global dict
            print("\nYour email has been changed successfully, returning to the previous menu.")
            return (Banking_System(username).change_details_menu())  # Returning to the menu they were last on

        elif user_option == "4":  # Triggers change in username
            new_username = input("Please enter your new username (minimum legth 5): ").strip()
            while (len(new_username) <= 5) and (new_username in global_customer_data): # Checking uname is an ok length
                new_username = input("Your username must be at least 5 characters. Please try again: ").strip()

            global_customer_data[new_username] = global_customer_data[username]  # Assigning new username its data
            global_customer_data.pop(username)  # Removing the old username and its data
            print("\nYour username has been changed successfully, returning to the previous menu.")
            password = global_customer_data[new_username]["Customer Information"]["Password"]
            self.write_to_csv(new_username, password)  # Writing the updated username to the csv file
            return (Banking_System(new_username).change_details_menu())  # Returing to the menu they were last on

        elif user_option == "5":  # Triggers change in password
            new_password = input("Please enter your new password (minimum legth 8): ").strip()
            while not len(new_password) >= 8: # Checking password is an ok length
                new_password = input("Your password must be at least 8 characters. Please try again: ").strip()

            global_customer_data[username]["Customer Information"]["Password"] = new_password  # Updating global dict
            print("\nYour password has been changed successfully, returning to the previous menu.")
            self.write_to_csv(username, new_password)  # Writing the updated password to the csv file
            return (Banking_System(username).change_details_menu())  # Returning to the menu they were last on

        elif user_option == "6":  # Triggers change in age
            new_age = input("Please enter your new age: ")
            while not new_age.isdigit():  # Checks the age is a positve integer
                new_age = input("Your age must be a positive, whole number. Please try again: ").strip()

            global_customer_data[username]["Customer Information"]["Age"] = new_age  # Updating global dict
            print("\nYour age has been changed successfully, returning to the previous menu.")
            return (Banking_System(username).change_details_menu())  # Returning to the menu they were last on

        elif user_option == "7":  # Triggers change in country of residence
            new_country = input("Please enter your new country of residence: ")
            while not (new_country.isalpha() and len(new_country) >= 1):  # Checking country of residence is ok format
                new_country = input("Your country of residence must contain only letters. Please try again: ").strip()

            global_customer_data[username]["Customer Information"]["Country"] = new_country  # Updating global dict
            print("\nYour country of residence has been changed successfully, returning to the previous menu.")
            return (Banking_System(username).change_details_menu())  # Returns to the meny they were last on

        elif user_option == "8":  # Triggers return to the main menu
            print("You chose to return to the main menu.")
            return (Banking_System(username).main_menu())  # Returns to the main meny

        else:  # Checks for bad inputs (letters, out of range numbers etc) and asks to try again
            return (self.change_account_details(username, input("Sorry, you appear to have made " +
                                                                "an invalid selection, please try again: ")))

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
                transaction_type = value["Previous Transaction"]["Transaction Type"]
                transaction_value = value["Previous Transaction"]["Transaction Value"]

                print(f"{key}:")
                print(f"Type: {wallet_type}")
                print("Balance: £{:,.2f}".format(balance))  # Makes the number a nice readable format with commas every 000
                print(f"The most recent transaction was: a {transaction_type}")
                print("The value of this transaction was: £{:,.2f}".format(transaction_value))
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

    def write_to_csv(self, username, password):

        encrypted_password = self.password_encryption(password)
        login_info = [username, password, encrypted_password]
        with open("customer_login_info.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(login_info)

    def password_encryption(self, password):
        """Defining the method of encryption for the password. It is a substitution cypher whos complexity and
        robustness depends on the key used in the encryption."""

        key = "AMNG186^%79HF@KLEP&VZ)#!RC"  # A key that involves non-alphabet chars is harder to brute force
        encrypted_password = ""
        for letter in password:
            if letter.isalpha():  # Checking for alphabet characters to shift
                letter_index = ord(letter.upper()) - ord('A')  # Finds position of the letter in the alphabet
                encrypted_letter = key[letter_index]  # Encrypted letter is the key letter in the same relative position
                if letter.islower():
                    encrypted_letter = encrypted_letter.lower()  # Reverts the case of the encrypted letter to original
                encrypted_password += encrypted_letter  # Adds the encrypted letter to the encrypted password
            else:
                encrypted_password += letter  # Adds non alphabet letters back to the password in the same place.
        return (encrypted_password)

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
        transaction_info = {}

        self.username = username
        self.wallet_id = wallet_id
        self.wallet_type = wallet_type
        self.balance = initial_deposit

        wallet_info["Wallet ID"] = self.wallet_id
        wallet_info["Wallet Type"] = self.wallet_type
        wallet_info["Balance"] = self.balance
        transaction_info["Transaction Type"] = "None"
        transaction_info["Transaction Value"] = 0
        wallet_info["Previous Transaction"] = transaction_info

        global_customer_data[self.username]["Associated Wallets"][self.wallet_id] = wallet_info
        print("\nYour wallet has been successfully created, returning to the previous menu.")

    def deposit(self, username, wallet_id):
        """Defining the function to allow customers to deposit funds to their wallet."""

        deposit_amount = float(input(f"Please enter how much money you woult like to deposit into {wallet_id}: "))
        if deposit_amount <= 0:
            print("\nYou cannot deposit a negative or null amount of money, please try again.")
            return (self.deposit(username, wallet_id))

        balance = global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"]
        balance += deposit_amount
        global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"] = balance
        print("\nThe deposit has been completed for you, returning to the previous menu.")

        transac_type = "deposit"
        return (self.previous_transaction(username, wallet_id, transac_type, deposit_amount),
                Banking_System(username).wallets_overview_menu())

    def withdraw(self, username, wallet_id):
        """Defining the function to allow customers to withdraw funds from their wallet. This function will
        be overwritten if the child wallet is not allowedd to execute on the coursework brief."""

        withdraw_amount = float(input(f"Please enter the amount of money you wish to withdraw from {wallet_id}: "))
        if withdraw_amount <= 0:
            print("\nYou cannot deposit a negative or null amount of money, please try again.")
            return (self.withdraw(username, wallet_id))

        balance = global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"]

        if (balance - withdraw_amount) >= 0:
            balance -= withdraw_amount
            global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"] = balance
            print("\nThe withdrawal has been completed for you, returning to the previous menu.")

            transac_type = "withdrawal"
            return (self.previous_transaction(username, wallet_id, transac_type, withdraw_amount),
                    Banking_System(username).wallets_overview_menu())

        else:
            print(f"\n{wallet_id} has insufficient funds to withdraw this amount. Please try again.")
            return (self.withdraw(username, wallet_id))

    def wallet_transfer(self, username, wallet_id):
        """Defining the function to allow customers to transfer funds from this wallet to another. This function will
        be overwritten if the child wallet is not allowedd to execute on the coursework brief."""

        target_wallet_id = input("Please enter the ID of the wallet you would like to transfer to: ")
        target_wallet_type = global_customer_data[username]["Associated Wallets"][target_wallet_id]["Wallet Type"]
        transfer_amount = float(input("Please enter money you would like to transfer " +
                                f"to {target_wallet_id} from {wallet_id}: "))
        if transfer_amount <= 0:
            print("\nYou cannot deposit a negative or null amount of money, please try again.")
            return (self.wallet_transfer(username, wallet_id))

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
        transfer_fee = round(0.005 * transfer_amount, 2)

        if (balance - (transfer_amount + transfer_fee)) >= 0:
            balance -= (transfer_amount + transfer_fee)
            global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"] = balance

            target_balance = global_customer_data[username]["Associated Wallets"][target_wallet_id]["Balance"]
            target_balance += transfer_amount
            global_customer_data[username]["Associated Wallets"][target_wallet_id]["Balance"] = target_balance

            print("\nThe wallet transfer has been completed for you, returning to the previous menu.")
            transac_type = "wallet transfer"
            return (self.previous_transaction(username, wallet_id, transac_type, transfer_amount),
                    self.previous_transaction(username, target_wallet_id, transac_type, transfer_amount),
                    Banking_System(username).transfer_fee_tracking(transfer_fee),
                    Banking_System(username).transfer_menu())

        else:
            print(f"\n{wallet_id} has insufficient funds to transfer this amount. Please try again.")
            return (self.wallet_transfer(username, wallet_id))

    def customer_transfer(self, username, wallet_id, target_username, target_wallet_id):
        """Defining the function to allow customers to transfer funds from this wallet to another. This function will
        be overwritten if the child wallet is not allowedd to execute on the coursework brief."""

        if (target_username in global_customer_data)\
        and (target_wallet_id in global_customer_data[target_username]["Associated Wallets"]):

            transfer_amount = float(input(f"Enter the amount you would like to transfer to {target_username}: "))
            if transfer_amount <=0:
                print("\nYou cannot deposit a negative or null amount of money, please try again.")
                return (self.customer_transfer(username, wallet_id, target_username, target_wallet_id))

            else:

                donor_balance = global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"]
                transfer_fee = round(0.015 * transfer_amount, 2)

                if (donor_balance - (transfer_amount + transfer_fee)) >= 0:
                    donor_balance -= (transfer_amount + transfer_fee)
                    global_customer_data[username]["Associated Wallets"][wallet_id]["Balance"] = donor_balance

                    target_balance = global_customer_data[target_username]["Associated Wallets"]\
                                                         [target_wallet_id]["Balance"]
                    target_balance += transfer_amount
                    global_customer_data[target_username]["Associated Wallets"]\
                                        [target_wallet_id]["Balance"] = target_balance

                    print(f"\nTransfer to {target_username} complete, returning to the previous menu.")
                    transac_type = "customer transfer"
                    return (self.previous_transaction(username, wallet_id, transac_type, transfer_amount),
                            self.previous_transaction(target_username, target_wallet_id, transac_type, transfer_amount),
                            Banking_System(username).transfer_fee_tracking(transfer_fee),
                            Banking_System(username).transfer_menu())

                else:
                    print(f"\n{wallet_id} has insufficient funds to transfer this amount. Please try again.")
                    return (self.customer_transfer(username, wallet_id, target_username, target_wallet_id))

        else:
            if not target_username in global_customer_data:
                print("\nThe user you have specified does not exist, returning to the previous menu.")
                return (Banking_System(username).transfer_menu())

            elif not target_wallet_id in global_customer_data[target_username]["Associated Wallets"]:
                print("\nThe user does not have a wallet with the ID you specified, returning to the previous menu.")
                return (Banking_System(username).transfer_menu())

    def delete_wallet(self, username, wallet_id):
        """Definition of the function to delete a user's wallet, if it exists."""

        global_customer_data[username]["Associated Wallets"].pop(wallet_id, None)  # sets the default to None
        print(f"\nIf you had a wallet with ID '{wallet_id}' it was deleted, returning to the previous menu")
        return (Banking_System(username).wallets_overview_menu())

    def previous_transaction(self, username, wallet_id, transaction_type, transaction_value):
        transaction_data = {}
        transaction_data["Transaction Type"] = transaction_type
        transaction_data["Transaction Value"] = transaction_value

        global_customer_data[username]["Associated Wallets"][wallet_id]["Previous Transaction"] = transaction_data

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
        self.total_fees_charged = global_customer_data["Bank"]["Associated Wallets"]["Fee Tracker"]["Balance"]

    def main_menu(self):
        """Defining the function to display the main menu"""

        print("1) View wallet options.")
        print("2) View transfer options.")
        print("3) Change your account details.")
        print("4) Log out of your account.")
        print("5) Delete your account.")
        user_option = input("Please select an option, 1 through 5: ").strip()

        if user_option == "1":
            print()
            return (self.wallets_overview_menu())

        elif user_option == "2":
            print()
            return (self.transfer_menu())

        elif user_option == "3":
            print()
            return (self.change_details_menu())

        elif user_option == "4":
            print()
            return (Customer_Account().log_out(self.username))

        elif user_option == "5":
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
            print("You chose to return to the main menu.")
            return (self.main_menu())

        else:
            print("Sorry, you appear to have made an invalid selection, please try again.")
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

    def change_details_menu(self):
        """Defining the menu function for changing account details."""

        print("1) Change forename.")
        print("2) Change surname.")
        print("3) Change eMail.")
        print("4) Change username.")
        print("5) Change password.")
        print("6) Change age.")
        print("7) Change country of residence.")
        print("8) Return to the previous menu")
        user_option = input("Please enter the number corresponding to the option you wish to choose: ")

        return (Customer_Account().change_account_details(self.username, user_option))

    def transfer_menu(self):
        """Defining function to display the transfer menu"""

        print("1) Transfer money between your wallets.")
        print("2) Transfer money to another customer.")
        print("3) Return to the previous menu")
        user_option = input("Please select an option, 1 through 3: ").strip()

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

    def transfer_fee_tracking(self, transfer_fee):
        self.total_fees_charged += transfer_fee
        global_customer_data["Bank"]["Associated Wallets"]["Fee Tracker"]["Balance"] = self.total_fees_charged

Customer_Account().login_menu()
