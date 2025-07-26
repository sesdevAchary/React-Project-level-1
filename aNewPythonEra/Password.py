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
    password= ''.join(random.choice(characters) for _ in range(length)) # or secret.choices
    # storing=mke one string-pick 1 rndm char(loop through len times)
    return password



#🎛 USER INTERACTION FUNCTION   #

def get_user_pref():
#Collects preferences from user via input(), handles errors, and prints/copies the password.
    try:
        length=int(input("🔢 Enter desired length of the password"))
        



    
    
    
    
    
    
    
    public static int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}public static int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
public static void calculator(char operator, double a, double b) {
    switch (operator) {
        case '+': System.out.println(a + b); break;
        case '-': System.out.println(a - b); break;
        case '*': System.out.println(a * b); break;
        case '/': System.out.println(b != 0 ? a / b : "Divide by zero!"); break;
        default: System.out.println("Invalid operator");
    }
}
public static int linearSearch(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
public static String reverse(String str) {
    return new StringBuilder(str).reverse().toString();
}
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}