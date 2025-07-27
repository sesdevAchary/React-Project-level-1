import random 
#For randomly selecting characters to form the password.secrets.choice() is more secure
import string
#Provides string constants like ascii_letters, digits, punctuation
import pyperclip
#Lets the program copy text to the clipboard.to copy the password after generation.

def generate_password(length, use_Letter=True,use_digits=True,use_symbols=True):
#include letters (A-Z, a-z),(0-9),!@#$%^&*()
#If arguments not passed when calling the function, it assumes you want to include that type of character.

    characters=' ' #Initializes an empty string to collect valid characters.acc to user
    
    if use_Letter:
        characters=characters+string.ascii_letters
    #if true then add a-z,A-Z to the empty char
    if use_digits:
        characters= characters+string.digits
    if use_symbols:
        characters=characters+string.punctuation
    if not characters:
        return "❌ Please select at least one character type."
    password= ''.join(random.choice(characters) for _ in range(length)) # or secret.choices
    # storing=mke one string-pick 1 rndm char(loop through len times)
    return password



#🎛 USER INTERACTION FUNCTION   #

def get_user_pref():
#Collects preferences from user via input(), handles errors, and prints/copies the password.
    try:
        
        length = int(input("🔢 Enter password length (e.g. 12): ").strip())

        use_Letter=(" Do you want to Input Letters ? (y/n)-> ").lower() =='y'
        use_digits=(" Do you want to Input Digits ? (y/n)-> ").lower() =='y'
        use_symbols=(" Do you want to Input symbols ? (y/n)-> ").lower() =='y'
        #Converts the user’s input to lower then compares Yes or No if yes then True otherwise false
        
        password= generate_password(length, use_Letter=True,use_digits=True,use_symbols=True)
        print("\n🔐 Generated Password:", password)
        
        
        copy = input(" Do you want to copy the password to your clipboard ?(y/n)->").lower()
        if copy == 'y':
            try:
                pyperclip.copy(password)
                print("📋 Password copied to clipboard!")
            except pyperclip.PyperclipException:
                print("⚠️ Clipboard not supported in this environment. Please copy manually.")   
            
    except ValueError:
        print("❌ Invalid input. Please enter numbers only for length.")
        
if __name__== "__main__":
    get_user_pref()
    
        



    
    
    
    
    
    