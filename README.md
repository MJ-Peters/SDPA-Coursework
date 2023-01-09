GitHub Repo Link: https://github.com/MJ-Peters/SDPA-Coursework
# SDPA Coursework Part 1 – Software Development
## Code Design
The money transfer system code is designed to function using three man types of classes: customer account, wallets, and banking system. In addition to this, there are four child wallet classes that make use of inheritance to allow for a more efficient design of code: daily use, savings, holidays, and mortgage. Each type of child wallet has different permissions therefore some of the wallets have to override inherited functions.
## Classes
### Customer Account
This class is responsible for the managing of a customers accound and their associated wallets (i.e. depositing/withdrawing/transfering) among wallets. 
### Wallets
The wallets parent class defines 7 methods to be inherited by its children. The first of which is the create wallets method. This method takes as arguments: the user’s username, the ID they’d like to assign their new wallet, the type of wallet they’d like to create, and the amount they’d like to deposit when opening the new wallet. The method then stores all the wallet data as a dictionary linked to the wallets ID, which is then stored in a dictionary of associated wallets, which is then stored in a dictionary linked to the customers username, which is finally stored in the global data store dictionary for all users.

The next method defined in the wallet parent class is the deposit method. This takes the username and the ID of the wallet to which the customer wishes to deposit. The function then asks for a deposit amount and, assuming a value greater than 0 was entered, the balance of the wallet is updated.

Following this, the withdraw method is defined. It works identically to the deposit method but adds a check ensuring that the wallet will not become overdrawn.

The wallet transfer method is more complicated, it combines aspects of both deposit and withdraw methods. The method takes as arguments: username and donor wallet ID. The method itself then asks the user to define the target wallet ID and transfer amount. The first thing done is fetch the wallet type for the specified target so that requests can be denied based on what it is allowed to receive. If both wallet types are good, the method then subtracts the transfer amount and transfer fee from the donor balance after checking that it won’t be overdrawn. The transfer amount is then added to the target wallets balance.

The customer transfer works almost the same as the wallet transfer. It takes additional arguments for the target user’s username and their wallet. The same checks from the previous method are then applied to the user’s wallets and the targets wallet.

The delete wallet method takes the user’s username and the ID of the wallet they’d like to delete. Pop is used to remove the wallet from the user’s dictionary, a default argument of none ensures that misinputs do not cause any errors.

The final method defined is to record and store the previous transaction done by or to the wallet. It takes the username, wallet ID, transaction type, and transaction value as arguments as they are all defined in the previous methods. This information is then attached to the wallet info dictionary.

As was mentioned earlier, different wallets have different permissions for methods according to the brief. These will be outlined in the following subsections.
#### Daily Use
Daily use is the most flexible type of wallet as it has access to all methods in the wallet parent class, thus no exceptions need be raised.
#### Savings
The savings wallet is not quite as flexible as the daily use class, it has its access to wallet and customer transfers restricted. These two methods get overwritten in a few lines of code and return an error message of they are called.
#### Holidays
The holidays wallet class is not so restrictive as the savings wallet class. It only has restrictions on customer transfers; therefore this is the only method that need be overwritten for this class.
#### Mortgage
The mortgage wallet class is by far the most restrictive, customers may only deposit into this wallet type. Withdraw, wallet transfer, and customer transfer are overwritten in this class.
### Banking System
This class is in charge of orchestrating the entire program. It is essentially a bunch of menu functions that take a users input and trigger the coinciding function in the account class which then triggers the wallet functions. On top of this, it countains a function that tracks the fees charged to a user every time they use a non-free service. If i had the time to improve this, I would make this function in charge of calculating the amount that needs to be charged rather than do so at the location where the function is called to make the code design more concise.

## Encryption Method
The encryption method chosen was the simple substitution cipher. This cipher involves replacing each letter in the original “plaintext” with a different letter or symbol to produce the “ciphertext”.

To implement this cipher in python, a function was defined to take in two arguments: the plaintext string and the 26 character encryption key string. The function iterates through each character in the plaintext and, if it is an alphabetic character, replaces it with the corresponding upper case character in the key string based on the index (position in the alphabet) of the original character. This upper-case ciphertext letter will then be lowered, assuming the plaintext letter is lowercase. If the character is non-alphabetic it is left unchanged in the ciphertext.

The robustness and complexity of the substitution cipher depend on the key used. A longer key will make it more difficult for an attacker to decrypt the ciphertext, but it will also make the cipher more complex to implement and use if it is longer than the alphabet. If the key is too short or predictable, it can be easily broken by an attacker using frequency analysis or brute force. The addition of non-alphabetic characters to the encryption key also makes it trickier to crack as attackers will find it harder to distinguish between encrypted and non-encrypted symbol characters.

Overall, the substitution cipher is a relatively simple and easy-to-implement encryption method; however, it is not robust against attacks and should not be used for secure communication. 

# SDPA Coursework Part 2 – Data Analysis
## External Libraries needed:
- BS4 (Beautiful Soup) for web scraping
- NumPy for data formatting
- Pandas for creating DataFrames
- MatPlotLib for plotting data
- venn3 from matplolib_venn for creating venn diagrams
- Seaborn for plotting data using matplotlib
- scipy for statistical testing
- pearsonr from scipy.stats for statistical testing
## Non External Libraries:
- csv to read/write to csv files
- re for string formatting
- math for checking NaN values
- requests for sending html requests