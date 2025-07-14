

expenses = []
# initiating a global list to store experience 

def add_expense();
 try:
     amount = float(input(" enter the expense amount:  "))
     # prompt the user ip- amount...convert to float
     # if user writes abc ip then it triggers the except bloack..
     category = input("Enter category (e.g., food, transport): ")
     date = input("Enter date (YYYY-MM-DD): ")
     
     
     
     
     
     
     
     
     def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci(10)
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  # True
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

print(is_prime(29))  # True
def calculator(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

print(calculator(10, 5, '*'))  # 50
from collections import Counter

text = "apple orange banana apple orange apple"
words = text.split()
print(Counter(words))
squares = [x**2 for x in range(10)]
print(squares)
squares = [x**2 for x in range(10)]
print(squares)
data = [(1, 3), (2, 2), (3, 1)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
