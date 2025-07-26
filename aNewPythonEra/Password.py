import random 
#For randomly selecting characters to form the password.secrets.choice() is more secure
import string
#Provides string constants like ascii_letters, digits, punctuation
import pyperclip
#Lets the program copy text to the clipboard.to copy the password after generation.

def generate_password(length, use_Letter=True,use_digits=True,use_symbols=True):
#include letters (A-Z, a-z),(0-9),!@#$%^&*()
#If arguments not passed when calling the function, it assumes you want to include that type of character.
    characters=''#Initializes an empty string to collect valid characters.acc to user
    if use_Letter:
        characters=characters+string.ascii_letters
    #if true then add a-z,A-Z to the empty char
    if use_digits:
        characters= characters+string.digits
    if use_symbols:
        characters=characters+string.punctuation
    if not characters:
        return "❌ Please select at least one character type."
    password= ''.join(random.choice(characters) for _ in range(length))
    # for in range the range times
    