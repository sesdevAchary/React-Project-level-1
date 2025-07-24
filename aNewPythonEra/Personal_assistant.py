## PERSONAL ASSISTANT CONSOLE APP....

import random   #Used to randomly pick a motivational quote.
import datetime 
import json
import os
NOTES_FILE = "notes.json"  # Global file name


quotes=[
    "Keep going, you're doing great!",
    "Stay positive and work hard.",
    "Success is a journey, not a destination.",
    "Believe in yourself!",
    "Every day is a second chance."
]


def greet_user():
    name =input("👋 Hello! What's your name?")
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
            content = file.read()
            if content.strip():
                print("📓 Your Notes:\n" + content)
            else:
                print("No notes yet")
    except FileNotFoundError:
        print("⚠️ No notes file found.")

def delete_saved_file():
    import os
    try:
        if os.path.exists("notes.txt"):
           os.remove("notes.txt")
           print("🗑️ Notes file deleted successfully.")
        else:
            print("⚠️ No notes file to delete.")
    except Exception as e:
        print("⚠️ Error deleting notes:", e)
        
def calaculator():
    try:
        expr=input(" 🧮 Enter a basic math expression (e.g.-> 5*8-9+2)")
        result = eval(expr)
        print(" 🧾 The result is:-> "+result)
    except:
        print("❌ Invalid expression.")
        
def search_notes():
    keyword=input(" Enter the word you want to search ").lower()
    notes=load_notes()
    found = false
    for note in notes:
        if keyword in notes['txt'].lower():
            print(f"✅ Found: {note['text']} (🕒 {note['timestamp']})")
            found =True
    if not found:
        print("❌ No matching notes found.")
        
def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4) 
    
def load_notes():
    if not os.path.exists([NOTES_FILE]):
        return []
    with open (NOTES_FILE,"r") as f:
        return json.load(f)

        
def show_menu():
    print("\n📌 What would you like to do?")
    print("1. Get a motivational quote")
    print("2. View current date and time")
    print("3. Write a note")
    print("4. Read saved notes")
    print("5. Deleting the Saved file")
    print("6. Use the Calculator")
    print("7. Exit")
    
user = greet_user()
print(f"Welcome ,{user} ! I am your personal assistant")
while True:
    show_menu()
    choice= input("enter your choice from (1 to 5):-> ")
    
    if choice =="1":
        show_quote()
    elif choice == "2":
        show_dateNtime()
    elif choice == "3":
        take_note()
    elif choice == "4":
        read_notes()
    elif choice == "5":
        delete_saved_file()
    elif choice == "6":
        calaculator()
    elif choice == "7":
        print(f"👋 Goodbye, {user}! Have a great day!")
        break
    else:
        print("❌ Invalid choice. Try again.")



        
    