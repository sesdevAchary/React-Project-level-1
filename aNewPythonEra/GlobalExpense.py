

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
 
     
     
     
     
     
     
     
    