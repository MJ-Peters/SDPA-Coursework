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
        """Initialise the attributes associated with the accounts."""
        self.forename = forename
        self.surname = surname
        self.email = email
        self.username = username
        self.password = password
        self.age = age
        self.country = country  # Country of residence of the account holder

        customer_info = {}  #  Dictionary for the storage of the customer data dictionary
        unique_customer_data = {}  # Dictionary for the storage of all customer dat (username, password etc)

        unique_customer_data["Username"] = self.username
        unique_customer_data["Password"] = self.password
        unique_customer_data["Forname"] = self.forename
        unique_customer_data["Surname"] = self.surname
        unique_customer_data["Email"] = self.email
        unique_customer_data["Age"] = self.age
        unique_customer_data["Country of Residence"] = self.country

        customer_info["Customer Information"] = unique_customer_data
        global_customer_data[self.username] = customer_info  # Link customer data with username to stores in global dict

    def log_in(self, username_input, password_input):
        """Function to allow customers to log in"""
        """
        Give permissions by having some variable default set to False that gets returned as True when
        Username and password are correct. Also need to make sure you cant just set the variable to true without
        using username and password. 
        """
        veriied = False  # Use this as the variable mentioned above, use better name if can think of one

        if (username_input in global_customer_data) and (global_customer_data[username_input]["Password"] == password_input):
            print("You have successfully logged in.")

        else:
            print("Your username or password was incorrect, please try again.")
            return(self.log_in(input("Please enter your username: "),
                               input("Please enter your password: ")))

    def log_out(self):
        """Function to allow customers to log out"""
        """First need to figure out a way to block access until logged in so it can be revoked by logout"""

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
    Definition of the Wallet parent class. The deposit function is the only capability shared by all wallets, so is
    the only one defined here so that the others obtain it through inheritance.
    """
    def __init__(self, wallet_id, wallet_type, initial_deposit):
        self.wallet_id = wallet_id
        self.wallet_type = wallet_type
        self.balance = initial_deposit

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def view_wallet_info(self):
        print()
        # Needs to search through the customer_wallet dictionary for specified wallet and display all it's information


test_account = Customer_Account("Test", "Account", "Test.Account@Test.com", "TestAccount", "Pword", 22, "UK")
print(global_customer_data)

log_in_test = test_account.log_in("TestAccount2", "Pword3")
