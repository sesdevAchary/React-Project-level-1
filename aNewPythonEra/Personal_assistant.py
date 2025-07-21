## PERSONAL ASSISTANT CONSOLE APP....

import random   #Used to randomly pick a motivational quote.
import datetime 

quotes=[
    "Keep going, you're doing great!",
    "Stay positive and work hard.",
    "Success is a journey, not a destination.",
    "Believe in yourself!",
    "Every day is a second chance."
]


def greeet_user():
    name =print(input("👋 Hello! What's your name?"))
    print(f"Welcome ,{name} ! I am your personal assistant ")
    return name
def show_quote():
    print("💡 Quote of the Day:")
    print(random.choice(quotes))
    
def show_dateNtime():
    now = datetime.datetime.now()
    print("📅 Current Date and Time:", now.strftime("%d-%m-%y:%H-%M-%S"))
    
def take_note():
    try:
        note = input("📝 Write your note: ")
        with open("notes.txt" ,"a") as file:
            file.write(note+"\n")
        print("✅ Note saved successfully!")
    except Exception as e:
         print("⚠️ Error saving note:", e)

def read_notes():
    try:
        with open("notes.txt","r") as file:
            if content.strip():
                print("📓 Your Notes:\n" + content)
            else:
                print("No notes yet")
    except FileNotFoundError:
        print("⚠️ No notes file found.")
        
        
        
        
        
        
        
        
        quotes = [
    "Believe you can and you're halfway there.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going."
]
def show_date_time():
    now = datetime.datetime.now()
    print("📅 Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
def show_quote():
    print("💡 Quote of the Day:")  # Step 1: Print a header
    print(random.choice(quotes))   # Step 2: Print a random quote
def take_note():
    try:
        note = input("📝 Write your note: ")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        print("✅ Note saved successfully!")
    except Exception as e:
        print("⚠️ Error saving note:", e)
def read_notes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
            if content.strip():
                print("📓 Your Notes:\n" + content)
            else:
                print("🗒️ No notes yet.")
    except FileNotFoundError:
        print("⚠️ No notes file found.")


public static boolean isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= Math.sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}
public static boolean isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= Math.sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}







