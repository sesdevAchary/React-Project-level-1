

expenses = []
# initiating a global list to store experience 

def add_expense():
   try:
     amount = float(input(" enter the expense amount:  "))
     # prompt the user ip- amount...convert to float
     # if user writes abc ip then it triggers the except bloack..
     category = input("Enter category (e.g., food, transport): ")
     date = input("Enter date (YYYY-MM-DD): ")
     expenses.append({"amount":amount, "catagory":catagory,"date":date})
     # creatin a dictionary in key-val pair usin { }
     print("Expenses Added:")
   except ValueError:
     print("Invalid input. Amount must be a number.")
     
     
# viewing the expense list
def view_expense():
  if not expense:
    print(" no expense required ")
    return
  for i,expenses in enumerate(expenses,start=1):
    print(f"{i}. {expenses['date']}-{expenses['catagory']}: ₹{expenses['amount']}")
    #enumerate() gives index and value after loopin through the list.
    #i = 1, expense = {"amount": 50, "category": "Food", ...}
    

def total_expense():
  total = sum(e['amount'] for e in expenses)
  print(f" Total expense is : ₹{total}")
  
  
#Save the global expenses list to this file.#
#This function converts your current in-memory list of expenses to a text format
#Then writes that to a file so you can keep the data even after closing the program
def save_to_file(filename="expenses.txt"):
#It takes one argument: filename, which defaults to "expenses.txt" if nothing is provided.
  try:
    with open(filename, 'w') as file:
      for e in expenses:
        file.write(f"{e['date']},{e['catagory']},{e['amount']}\n")
    print("💾 Expenses saved to file.")
  except Exception as e:
    print("❌ Error saving to file:", e)
 
     
     
#Restore the expense list from a file to reuse again 
def load_from_file(filename="expenses.txt"):
#load_from_file("myfile.txt")  # loads from another file
  try:
    with open(filename,'r') as file:
      for line in file:
        date,catagory,amount = line.strip().split(',')
        expenses.append({
          "date":date,
          "category":catagory,
          "amount":float(amount)
        })
    print("📂expenses loaded from file")   
  except FileNotFoundError:
    print("⚠️ No saved file found.")
  except Exception as e:
    print("❌ Error loading from file:", e)   
     
     
# main menu loop 
def main():
  while True:
    print("\n--------------PERSONAL EXPENSE TRACKER--------------")
    print("1. Add Expenses ")
    print("2. view Expenses ")
    print("3. Total Expenses ")
    print("4. Save Expenses ")
    print("5. Load Expenses ")
    print("6. Exit ")
    choice = input("👉 Choose an option (1-6): ")
    
    if choice == '1':
      add_expense()
    if choice == '2':
      view_expense()
    if choice == '3':
      total_expense
    if choice == '4':
      save_to_file()
    if choice == '5':
      load_from_file()
    if choice == '6':
      print("👋 Exiting... Thank you for using the Expense Tracker!")
      break
    else:
      print("❌ Invalid choice. Please enter a number from 1 to 6.")
      
# Run the program
if __name__ == "__main__":
    main()
    