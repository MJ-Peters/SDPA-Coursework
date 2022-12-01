""""
SDPA Final Coursework Part A: Money Transfer System
Student: Marshall James Peters
Student ID: 2272289
"""
customer_data = {}
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

        unique_customer_data = {}  # Empty dictionary where customer data can be paired and stored

        unique_customer_data["Password"] = self.password
        unique_customer_data["Forname"] = self.forename
        unique_customer_data["Surname"] = self.surname
        unique_customer_data["Email"] = self.email
        unique_customer_data["Age"] = self.age
        unique_customer_data["Country of Residence"] = self.country

        customer_data[self.username] = unique_customer_data  # Link customer data with username to stores in global dict

    def log_in(self, username_input, password_input):
        """Function to allow customers to log in"""

        if (username_input in customer_data) and (customer_data[username_input]["Password"] == password_input):
            print("You have successfully logged in.")

        else:
            print("Your username or password was incorrect, please try again.")
            return(self.log_in(input("Please enter your username: "),
                               input("Please enter your password: ")))

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

test_account = Customer_Account("Test", "Account", "Test.Account@Test.com", "TestAccount", "Pword", 22, "UK")
test_account = Customer_Account("Test2", "Account2", "Test.Account2@Test.com", "TestAccount2", "Pword2", 23, "UK")
print(customer_data)

log_in_test = test_account.log_in("TestAccount2", "Pword3")
