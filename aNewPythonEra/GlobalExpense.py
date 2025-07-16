

expenses = []
# initiating a global list to store experience 

def add_expense():
   try:
     amount = float(input(" enter the expense amount:  "))
     # prompt the user ip- amount...convert to float
     # if user writes abc ip then it triggers the except bloack..
     category = input("Enter category (e.g., food, transport): ")
     date = input("Enter date (YYYY-MM-DD): ")
     expenses.append({"amount":amount, "category": category,"date":date})
     # creatin a dictionary in key-val pair usin { }
     print("Expenses Added:")
   except ValueError:
     print("Invalid input. Amount must be a number.")
     
     
# viewing the expense list
def view_expense():
  if not expenses:
    print("⚠️ No expenses recorded.")
    return
  for i,expense in enumerate(expenses,start=1):
    print(f"{i}. {expense['date']}-{expense['category']}: ₹{expense['amount']}")
    #enumerate() gives index and value after loopin through the list.
    #i = 1, expense = {"amount": 50, "category": "Food", ...}
    

def total_expense():
  total = sum(e['amount'] for e in expenses)
  print(f"💰 Total expense is: ₹{total:.2f}")
  
  
#Save the global expenses list to this file.#
#This function converts your current in-memory list of expenses to a text format
#Then writes that to a file so you can keep the data even after closing the program
def save_to_file(filename="expenses.txt"):
#It takes one argument: filename, which defaults to "expenses.txt" if nothing is provided.
  try:
    with open(filename, 'w') as file:
      for e in expenses:
        file.write(f"{e['date']},{e['category']},{e['amount']}\n")
    print("💾 Expenses saved to file.")
  except Exception as e:
    print("❌ Error saving to file:", e)
 
     
     
#Restore the expense list from a file to reuse again 
def load_from_file(filename="expenses.txt"):
#load_from_file("myfile.txt")  # loads from another file
  try:
    with open(filename,'r') as file:
      for line in file:
        date,category,amount = line.strip().split(',')
        expenses.append({
          "date":date,
          "category":category,
          "amount":float(amount)
        })
    print("📂expenses loaded from file")   
  except FileNotFoundError:
    print("⚠️ No saved expense file found. Start by adding new expenses.")
  except Exception as e:
    print("❌ Error loading from file:", e)   
    
    
def delete_expense():
  view_expense():
    try:
      index=int(input("enter the number of the input to delete"))
      if 1<=index<=len(expenses):
        removed=expenses.pop(index-1)
        print(f"🗑️ Deleted: {removed['date']} - {removed['category']} - ₹{removed['amount']}")
      else:
        print("invalid index")
    except ValueError:
      print("❌ Please enter a valid number.")
      
     
     
# main menu loop 
def main():
  while True:
    print("\n====== PERSONAL EXPENSE TRACKER ======")
    print("1. Add Expenses ")
    print("2. view Expenses ")
    print("3. Total Expenses ")
    print("4. Save Expenses ")
    print("5. Load Expenses ")
    print("6. Delete Expenses ")
    print("7. Exit ")
    choice = input("👉 Choose an option (1-7): ")
    
    if choice == '1':
      add_expense()
    elif choice == '2':
      view_expense()
    elif choice == '3':
      total_expense()
    elif choice == '4':
      save_to_file()
    elif choice == '5':
      load_from_file()
    elif choice == '6':  
      delete_expense()
    elif choice == '7':
      print("👋 Exiting... Thank you for using the Expense Tracker!")
      break
    else:
      print("❌ Invalid choice. Please enter a number from 1 to 6.")
      
# Run the program
if __name__ == "__main__":
    main()
    
#Only run the main() function if this file is run directly — not if it's being imported into another file

#__name__:
#A built-in special variable in Python.

#When a Python file is executed directly, __name__ becomes "__main__".

#When a Python file is imported into another Python file, __name__ becomes the name of the module (e.g., "expense_tracker").

#if __name__ == "__main__":
#This checks: “Am I running this file directly?”

#If yes → call main()








tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted: {removed}")
    else:
        print("Invalid task number.")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
import random
import string

length = int(input("Password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))
print("Generated password:", password)
import random

number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    tries += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {tries} tries.")
        break
events = {}

def add_event():
    date = input("Enter date (YYYY-MM-DD): ")
    event = input("Enter event description: ")
    events.setdefault(date, []).append(event)

def view_events():
    for date in sorted(events):
        print(f"{date}:")
        for event in events[date]:
            print(f"  - {event}")

while True:
    print("\n1. Add Event\n2. View Events\n3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_event()
    elif choice == "2":
        view_events()
    elif choice == "3":
        break
import csv

def add_expense():
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        amount = input("Amount: ")
        category = input("Category: ")
        date = input("Date (YYYY-MM-DD): ")
        writer.writerow([amount, category, date])
        print("Expense added!")

def view_expenses():
    try:
        with open("expenses.csv", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                print(f"₹{row[0]} - {row[1]} - {row[2]}")
    except FileNotFoundError:
        print("No expenses found.")

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
import os
import shutil

def organize(folder_path):
    for filename in os.listdir(folder_path):
        name, ext = os.path.splitext(filename)
        ext = ext[1:]
        if ext:
            folder = os.path.join(folder_path, ext + "_files")
            os.makedirs(folder, exist_ok=True)
            shutil.move(os.path.join(folder_path, filename), os.path.join(folder, filename))

folder_path = input("Enter folder path: ")
organize(folder_path)
print("Files organized!")
