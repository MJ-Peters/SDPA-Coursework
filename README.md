# SDPA Coursework Part 1 – Software Development
## Code Design
## Classes
### Customer Account
### Wallets
### Banking System
## Methods
### Method A
### Method B
## Encryption Method
The encryption method chosen was the simple substitution cipher. This cipher involves replacing each letter in the original “plaintext” with a different letter or symbol to produce the “ciphertext”.
To implement this cipher in python, a function was defined to take in two arguments: the plaintext string and the 26 character encryption key string. The function iterates through each character in the plaintext and, if it is an alphabetic character, replaces it with the corresponding upper case character in the key string based on the index (position in the alphabet) of the original character. This upper-case ciphertext letter will then be lowered, assuming the plaintext letter is lowercase. If the character is non-alphabetic it is left unchanged in the ciphertext.
The robustness and complexity of the substitution cipher depend on the key used. A longer key will make it more difficult for an attacker to decrypt the ciphertext, but it will also make the cipher more complex to implement and use if it is longer than the alphabet. If the key is too short or predictable, it can be easily broken by an attacker using frequency analysis or brute force. The addition of non-alphabetic characters to the encryption key also makes it trickier to crack as attackers will find it harder to distinguish between encrypted and non-encrypted symbol characters.
Overall, the substitution cipher is a relatively simple and easy-to-implement encryption method; however, it is not robust against attacks and should not be used for secure communication. 

# SDPA Coursework Part 2 – Data Analysis
