

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
 
     
     
     
     
     
     
     
    