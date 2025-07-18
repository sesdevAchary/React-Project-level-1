

# expenses = []
# # initiating a global list to store experience 

# def add_expense():
#    try:
#      amount = float(input(" enter the expense amount:  "))
#      # prompt the user ip- amount...convert to float
#      # if user writes abc ip then it triggers the except bloack..
#      category = input("Enter category (e.g., food, transport): ")
#      date = input("Enter date (YYYY-MM-DD): ")
#      expenses.append({"amount":amount, "category": category,"date":date})
#      # creatin a dictionary in key-val pair usin { }
#      print("Expenses Added:")
#    except ValueError:
#      print("Invalid input. Amount must be a number.")
     
     
# # viewing the expense list
# def view_expense():
#   if not expenses:
#     print("⚠️ No expenses recorded.")
#     return
#   for i,expense in enumerate(expenses,start=1):
#     print(f"{i}. {expense['date']}-{expense['category']}: ₹{expense['amount']}")
#     #enumerate() gives index and value after loopin through the list.
#     #i = 1, expense = {"amount": 50, "category": "Food", ...}
    

# def total_expense():
#   total = sum(e['amount'] for e in expenses)
#   print(f"💰 Total expense is: ₹{total:.2f}")
  
  
# #Save the global expenses list to this file.#
# #This function converts your current in-memory list of expenses to a text format
# #Then writes that to a file so you can keep the data even after closing the program
# def save_to_file(filename="expenses.txt"):
# #It takes one argument: filename, which defaults to "expenses.txt" if nothing is provided.
#   try:
#     with open(filename, 'w') as file:
#       for e in expenses:
#         file.write(f"{e['date']},{e['category']},{e['amount']}\n")
#     print("💾 Expenses saved to file.")
#   except Exception as e:
#     print("❌ Error saving to file:", e)
 
     
     
# #Restore the expense list from a file to reuse again 
# def load_from_file(filename="expenses.txt"):
# #load_from_file("myfile.txt")  # loads from another file
#   try:
#     with open(filename,'r') as file:
#       for line in file:
#         date,category,amount = line.strip().split(',')
#         expenses.append({
#           "date":date,
#           "category":category,
#           "amount":float(amount)
#         })
#     print("📂expenses loaded from file")   
#   except FileNotFoundError:
#     print("⚠️ No saved expense file found. Start by adding new expenses.")
#   except Exception as e:
#     print("❌ Error loading from file:", e)   
    
    
# def delete_expense():
#   view_expense()
#   try:
#       index=int(input("enter the number of the input to delete"))
#       if 1<=index<=len(expenses):
#         removed=expenses.pop(index-1)
#         print(f"🗑️ Deleted: {removed['date']} - {removed['category']} - ₹{removed['amount']}")
#       else:
#         print("invalid index")
#   except ValueError:
#       print("❌ Please enter a valid number.")
      
#  # Edit an expense by index
# def edit_expense():
#   view_expense()  ## Show current expenses
#   try:
#     index= int(input("enter the number of track you want to edit from 1-7"))
#     if(1<=index<=len(expenses)):
#       expense = expenses[index-1]
#       print("Leave the input empty if you want to keep the current update")
      
#       new_amount=input(f"New amount(current:{expense['amount']}):").strip()
#       #New amount(current:80.0):90
#       new_category=input(f"new category (current:{expense['category']}):").strip()
#       new_date=input(f"new date (current:{expense['date']}):").strip()
      
#       if new_amount:
#         #Checks if user typed something for the amount.if yes then update the value
#         try:
#           expense['amount']=float(new_amount)# updates the amount in the expense dictionary.
#         except ValueError:
#           print("❌ Invalid amount entered. Keeping previous value.")
#       if new_category:
#         expense['category']=new_category#If the user entered a new category, update the value.
#       if new_date:
#         expense['date']=new_date #only updates date if user typed a new one.
        
#       print(" ✅ Expenses are updated")
#     else:
#       print("❌ Invalid index.")
#   except ValueError: 
#     print("❌ not a valid number, Please enter a valid number. ")

      
     
# # main menu loop 
# def main():
#   while True:
#     print("\n====== PERSONAL EXPENSE TRACKER ======")
#     print("1. Add Expenses ")
#     print("2. view Expenses ")
#     print("3. Total Expenses ")
#     print("4. Save Expenses ")
#     print("5. Load Expenses ")
#     print("6. Delete Expenses ")
#     print("7. Edit Expenses ")
#     print("8. Exit ")
#     choice = input("👉 Choose an option (1-8): ")
    
#     if choice == '1':
#       add_expense()
#     elif choice == '2':
#       view_expense()
#     elif choice == '3':
#       total_expense()
#     elif choice == '4':
#       save_to_file()
#     elif choice == '5':
#       load_from_file()
#     elif choice == '6':  
#       delete_expense()
#     elif choice == '7':
#       edit_expense()  
      
#     elif choice == '8':
#       print("👋 Exiting... Thank you for using the Expense Tracker!")
#       break
#     else:
#       print("❌ Invalid choice. Please enter a number from 1 to 8.")
      
# # Run the program
# if __name__ == "__main__":
#     main()
    
# #Only run the main() function if this file is run directly — not if it's being imported into another file

# #__name__:
# #A built-in special variable in Python.

# #When a Python file is executed directly, __name__ becomes "__main__".

# #When a Python file is imported into another Python file, __name__ becomes the name of the module (e.g., "expense_tracker").

# #if __name__ == "__main__":
# #This checks: “Am I running this file directly?”

# #If yes → call main()



    



# tasks = []

# def add_task():
#     task = input("Enter task: ")
#     tasks.append({"task": task, "done": False})

# def view_tasks():
#     for i, t in enumerate(tasks, 1):
#         status = "✓" if t["done"] else "✗"
#         print(f"{i}. {t['task']} [{status}]")

# def mark_done():
#     view_tasks()
#     index = int(input("Enter task number to mark as done: ")) - 1
#     tasks[index]["done"] = True

# while True:
#     print("\n1.Add 2.View 3.Done 4.Exit")
#     choice = input("Choice: ")
#     if choice == "1": add_task()
#     elif choice == "2": view_tasks()
#     elif choice == "3": mark_done()
#     elif choice == "4": break
# from forex_python.converter import CurrencyRates
# c = CurrencyRates()

# amount = float(input("Amount: "))
# from_curr = input("From (e.g., USD): ").upper()
# to_curr = input("To (e.g., INR): ").upper()

# result = c.convert(from_curr, to_curr, amount)
# print(f"{amount} {from_curr} = {result:.2f} {to_curr}")
# import random

# number = random.randint(1, 100)
# attempts = 0

# while True:
#     guess = int(input("Guess a number (1-100): "))
#     attempts += 1
#     if guess < number:
#         print("Too low!")
#     elif guess > number:
#         print("Too high!")
#     else:
#         print(f"Correct! Guessed in {attempts} attempts.")
#         break
# import random
# import string

# length = int(input("Password length: "))
# characters = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choice(characters) for _ in range(length))
# print("Generated password:", password)
# import requests
# from bs4 import BeautifulSoup

# res = requests.get("https://www.bbc.com/news")
# soup = BeautifulSoup(res.text, 'html.parser')

# headlines = soup.find_all('h3')
# for h in headlines[:10]:
#     print(h.get_text(strip=True))
# import sqlite3

# conn = sqlite3.connect("expenses.db")
# c = conn.cursor()
# c.execute("CREATE TABLE IF NOT EXISTS expenses (amount REAL, category TEXT, date TEXT)")

# def add_expense():
#     a = float(input("Amount: "))
#     cat = input("Category: ")
#     date = input("Date (YYYY-MM-DD): ")
#     c.execute("INSERT INTO expenses VALUES (?, ?, ?)", (a, cat, date))
#     conn.commit()

# def view():
#     for row in c.execute("SELECT * FROM expenses"):
#         print(row)

# while True:
#     ch = input("\n1.Add 2.View 3.Exit\nChoice: ")
#     if ch == "1": add_expense()
#     elif ch == "2": view()
#     else: break

# conn.close()
# def respond(msg):
#     if "hello" in msg.lower():
#         return "Hi there!"
#     elif "bye" in msg.lower():
#         return "Goodbye!"
#     else:
#         return "I don't understand."

# while True:
#     user = input("You: ")
#     if user.lower() == "exit":
#         break
#     print("Bot:", respond(user))





class Track_Expense:
    def __init__(self):  #cons->__init__: Special method that runs when an object is created.
        self.expense = []

    def add_expense(self):  ##adding the expense# 
      #self refers to the current instance of the class. access to the instance’s variables
      #Adds the new expense as a dictionary to the list self.expenses,
      # which is an instance variable initialized in the class (likely in __init__()).
        try:
            amount = float(input("Enter the expense amount:-> "))
            category = input("Enter the category (e.g.-Food, Transport):-> ")
            date = input("Enter the date 📅 (DD-MM-YYYY format):-> ")
            self.expense.append({
                "amount": amount,
                "category": category,
                "date": date
            })
            print("✅ Expense added!")
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")

def view_expense(self):
    if not self.expense: #checks if the list is empty.
        print("📭 No expenses recorded.")
        return
    print("\n📋 Expense History:")
    for i,e in enumerate(self.expense,start =1): # index e-item value in enumerate
        print(f"{i}->{e['date']},{e['category']}- ₹{e['amount']}:.3f")
        
def total_expense(self):
    total = sum(e['amount'] for e in self.expense)
    print(f"💰 Total expenses: ₹{total:.2f}")
    
def save_to_file(self ,filename="expense.txt"): #optionally accepts a filename 
    try:
        with open(filename,'w') as file:
            for e in self.expense:
                file.write(f"{e['date']},{e['category']},{e['amount']}\n")
        print("💾 Expenses saved to file.")
    except Exception as e:
        print("❌ Error saving to file:", e) 
        
        
        
        
        
        
        
        
        
        import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow('Face Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
def respond(msg):
    if "hello" in msg.lower():
        return "Hi there!"
    elif "bye" in msg.lower():
        return "Goodbye!"
    else:
        return "I don't understand."

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    print("Bot:", respond(user))
import sqlite3

conn = sqlite3.connect("expenses.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS expenses (amount REAL, category TEXT, date TEXT)")

def add_expense():
    a = float(input("Amount: "))
    cat = input("Category: ")
    date = input("Date (YYYY-MM-DD): ")
    c.execute("INSERT INTO expenses VALUES (?, ?, ?)", (a, cat, date))
    conn.commit()

def view():
    for row in c.execute("SELECT * FROM expenses"):
        print(row)

while True:
    ch = input("\n1.Add 2.View 3.Exit\nChoice: ")
    if ch == "1": add_expense()
    elif ch == "2": view()
    else: break

conn.close()

        
