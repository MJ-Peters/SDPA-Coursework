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

        customer_data = {}  #  Dictionary for the storage of the customer data dictionary
        unique_customer_info = {}  # Dictionary for the storage of all customer dat (username, password etc)

        unique_customer_info["Username"] = self.username
        unique_customer_info["Password"] = self.password
        unique_customer_info["Forname"] = self.forename
        unique_customer_info["Surname"] = self.surname
        unique_customer_info["Email"] = self.email
        unique_customer_info["Age"] = self.age
        unique_customer_info["Country of Residence"] = self.country

        customer_data["Customer Information"] = unique_customer_info
        global_customer_data[self.username] = customer_data  # Link customer data with username to stores in global dict

    def log_in(self, username_input, password_input):
        """Function to allow customers to log in"""
        """
        Give permissions by having some variable default set to False that gets returned as True when
        Username and password are correct. Also need to make sure you cant just set the variable to true without
        using username and password. 
        """
        veriied = False  # Use this as the variable mentioned above, use better name if can think of one

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
    def __init__(self, wallet_id, wallet_type, initial_deposit):
        """Initialising the Wallet class with relevant details to identify a wallet"""
        self.wallet_id = wallet_id
        self.wallet_type = wallet_type
        self.balance = initial_deposit

    def deposit(self, deposit_amount, target_wallet_id):
        """Definig the deposit function, which all wallet types will gain through inheritance"""
        """
        In pracitce may need changing as unsure how to target the balance of the specified wallet, whether this is done
        using self.balance or by directly accessing the dictionary where the balance is stored.
        """
        self.deposit_amount = deposit_amount
        self.target_wallet_id = target_wallet_id
        # self.balance += deposit_amount

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

    def withdraw(self, withdraw_amount, wallet_id):
        """Defining the function to allow customers to withdraw funds from this wallet type."""
        self.withdraw_amount = withdraw_amount
        self.wallet_id = wallet_id

    def wallet_transfer(self, transfer_amount, donor_wallet_id, target_wallet_id):
        """Defining the function to allow customers to withdraw funds from this wallet type"""
        """
        Take into considerations the target wallet type limitations, check the type in this function. Also 0.5% fee
        """
        self.transfer_amount = transfer_amount
        self.donor_wallet_id = donor_wallet_id
        self.target_wallet_id = target_wallet_id

    def customr_transfer(self, transfer_amount, donor_wallet_id, target_customer_username):
        """
        Might need to specify the recieving customers wallet id if you are unable to figure out how to default
        to their daily use wallet. Don't forget wallet type limitations.
        """
        """
        Take into considerations the target wallet type limitations, check the type in this function. Also 1.5% fee
        """
        self.transfer_amount = transfer_amount
        self.donor_wallet_id = donor_wallet_id
        self.target_customer_username = target_customer_username
        print()

test_account = Customer_Account("Test", "Account", "Test.Account@Test.com", "TestAccount", "Pword", 22, "UK")
print(global_customer_data)

log_in_test = test_account.log_in("TestAccount2", "Pword3")
