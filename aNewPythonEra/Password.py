import random 
#For randomly selecting characters to form the password.secrets.choice() is more secure
import string
#Provides string constants like ascii_letters, digits, punctuation
import pyperclip
#Lets the program copy text to the clipboard.to copy the password after generation.

def generate_password(length, use_Letter=True,use_digits=True,use_symbols=True):
    characters=''
    