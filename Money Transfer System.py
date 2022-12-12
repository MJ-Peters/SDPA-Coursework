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
        self.forename = forename
        self.surname = surname
        self.email = email
        self.username = username
        self.password = password
        self.age = age
        self.country = country  # Country of residence of the account holder

        customer_data = {}  #  Dictionary for the storage of the customer data dictionary
        unique_customer_info = {}  # Dictionary for the storage of all customer dat (username, password etc)

        unique_customer_info["Username"] = self.username
        unique_customer_info["Password"] = self.password
        unique_customer_info["Forename"] = self.forename
        unique_customer_info["Surname"] = self.surname
        unique_customer_info["Email"] = self.email
        unique_customer_info["Age"] = self.age
        unique_customer_info["Country of Residence"] = self.country

        customer_data["Customer Information"] = unique_customer_info
        global_customer_data[self.username] = customer_data  # Link customer data with username to stores in global dict

        # Creating the users first wallet so that "Associated Wallets" exists and can be added to later on.
        wallet_info = {}
        new_wallet = {}
        wallet_info["Wallet ID"] = "Daily Use 1"
        wallet_info["Wallet Type"] = "Daily Use"
        wallet_info["Balance"] = 0

        new_wallet[f"{self.username}'s Daily Use 1"] = wallet_info

        global_customer_data[self.username]["Associated Wallets"] = new_wallet

    def log_in(self, username_input, password_input):
        """Function to allow customers to log in"""
        """
        Give permissions by having some variable default set like "verified = False" that gets returned as True when
        Username and password are correct. Also need to make sure you cant just set the variable to true without
        using username and password. 
        """
        """
        OR (probably better) once login is successful pull the "username": {data} dictionary as a dictionary called 
        "accessible_data" which is the only stuff they have access to, to ensure they have access to only their own 
        info and money.
        """
        """
        OR some combination of both? Not sure if that is possible, might not be neccesary.
        """

        if (username_input in global_customer_data) and\
           (global_customer_data[username_input]["Customer Information"]["Password"] == password_input):
            print("You have successfully logged in.")

        else:
            print("Your username or password was incorrect, please try again.")
            return(self.log_in(input("Please enter your username: "),
                               input("Please enter your password: ")))

    def log_out(self):
        """Function to allow customers to log out"""
        """First need to figure out a way to block access until logged in so it can be revoked by logout"""

    def change_account_details(selfself):
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

    def __init__(self, username, wallet_id, wallet_type, initial_deposit):
        """Initialising the Wallet class with relevant details to identify a wallet"""
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

    def deposit(self, deposit_amount):
        """Definig the deposit function, which all wallet types will gain through inheritance"""
        """
        In pracitce may need changing as unsure how to target the balance of the specified wallet, whether this is done
        using self.balance or by directly accessing the dictionary where the balance is stored. Need to check if wallet
        ID exists and ask for another if it does not.
        """

        self.balance += deposit_amount
        global_customer_data[self.username]["Associated Wallets"][self.wallet_id]["Balance"] = self.balance

    def view_wallet_info(self):
        """Defining the function to allow customers to see an overview of all their wallets (i.e id, type, balance)."""
        print()

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
            print("fail")


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


# Creating some test accounts, wallets, and actions

test_account = Customer_Account("Test", "Account", "Test.Account@Test.com", "TestAccount", "Pword", 22, "UK")
new_wallet = Daily_Use("TestAccount", "TestAccount's Daily Use 2", "Daily Use", 100)
new_wallet = Savings("TestAccount", "TestAccount's Savings", "Savings", 200)
new_wallet = Holidays("TestAccount", "TestAccount's Holidays", "Holidays", 300)
new_wallet = Mortgage("TestAccount", "TestAccount's Mortgage", "Mortgage", 400)

test_account = Customer_Account("Test2", "Account2", "Test2.Account@Test.com", "TestAccount2", "Pword2", 22, "UK")

print(global_customer_data["TestAccount"])
print(global_customer_data["TestAccount2"])





# When it comes to integrating an interface class, new_wallet can be used for all wallets as it will be reset when
# the next new wallet needs creating. Still need to figure out how to have more than one wallet to a customer.

