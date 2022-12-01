""""
SDPA Final Coursework Part A: Money Transfer System
Student: Marshall James Peters
Student ID: 2272289
"""

class Customer_Account:
    """
    Definiton of the Customer Account class. Data associated with each customer account is stored so that customers
    may log out and back in with their wallets and their contents still being in tact. Calling this class with all
    necessary details 'creates' the customer account. No data persistance after closing script down is needed.
    """

    def __init_(self, forename, surname, country, age, email, username, password):
        """Initialise the attributes associated with the accounts."""
        self.forename = forename
        self.surname = surname
        self.country = country  # Country of residence of the account holder
        self.age = age
        self.email = email
        self.username = username
        self.password = password

    def log_in(self):
        """Function to allow customers to log in"""

    def log_out(self):
        """Function to allow customers to log out"""

    def create_wallet(self):
        """Function to allow customers to create a wallet of specified type"""

    def delete_wallet(self):
        """Function to allow customers to delete a specified wallet"""

    def wallet_details(self):
        """Function to allow customers to see an overview of all their wallets"""

    def deposit(self):
        """Function to allow customers to deposit money to a specified wallet, daily use being the default."""

    def withdraw(self):
        """Function to allow customers to withdraw money from a specified walled, daily use being the default"""

    def transfer_wallet(self):
        """Function to allow customers to transfer money from one specified wallet to another"""
