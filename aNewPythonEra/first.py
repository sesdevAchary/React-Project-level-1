# # # a= 5
# # # b=3
# # # sum = a+b
# # # print("sum =", sum)


# # # a= int(input("enter your number= "))
# # # b= int(input(" enter your second number="))

# # # if a > b:
# # #   print("larger num is a:",a)
# # # else:
# # #   print("larger number is b:",b)


# # a= int(input(" first number is "))
# # b= int(input("second numeber is "))
# # c= int(input("third number is"))



# name = "PsychoKiller"
# # nameO=''.join(reversed(name))
# # nameO= name[1:5] # starting from 1 to 4 excluding 5
# print(name.endswith("a")) #gives True or False


# a= [ "Ashwini" , "Rahul" , 0.55874, 54]
# print (a)
# print(type(a))    ## List Type ##



# a=  ("Ashwini" , "Rahul" , 0.55874, 54)
# print (a)
# print(type(a))         ## Tupple  Type ##




# marks = []
# # F = int(input( " mark in History:"))  one kind of input method orrrrrrr

# F=input("marks:")
# marks.append(F)
# print (marks)

# marks = [ 1,2,3,4,5]
# print(sum(marks))



# words= {
#     "India":"Delhi",
#     "Hungary":"Budapest",
#     "Iran":"Tehran",}
    
# word=input("enter the country name - ")
# print(words[word]) # it will print the capital of only the desired word country name 



# marks= int(input("enter your marks here"))
# if(marks>=90): 

#  print("Conrgrats you secured Grade A")


# elif(marks>=80):
#  print("Congrats you secured Grade B")

# elif(marks>=600):

#  print("Congrats you secured Grade C")

# elif(marks>=50):

#  print("Congrats you secured Grade D")

# else:

#  print("you were disavowed")

# age = int(input(" enter the number "))

#  if num > 0:
#   if num %2 == 0:
#    print("even number")
#   else:
#    print("odd number")

#  else:
#     print("negative number ")


# has_id= True
# if age>=18 and has_id:
#     print("ready to proceed ")
# else:
#     print("you are disavowed")
    
    
# mark1= int(input("enter first mark"))
# mark2= int(input("enter second  mark"))
# mark3= int(input("enter third mark"))

# percentage= 100 * ((mark1+mark2+mark3)/300)
# print("your percentage is :", percentage)

# if percentage>33:
#     print("Passed")
# else:
#     print("fail")

# name=input("enter your name")

# if len(name)>6:
#     print("more")
# else:
#     print("less")

# for i in range (89 , 180):
#     print(i)
    
# sum = 0
# for i in range (100):
#  sum+=i
#  print(sum)


# for i in range (3):
#      for j in range (3):
#         print(f"({i}, {j})", end=' ')   
# print()
      
 
 
# n = int(input("enter the number: "))
# for i in range(11):
#         print(f"{n}*{i}={n*i}")
#         #a formatted string (f-string).It evaluates expressions inside {} and replaces them with the values.#
   
   
   
   
# n = int ( input("enter a number-> "))

# for i in range (2,n):
#         if(n%i==0):
#                 print(" n is not a prime number")
#                 break;
# else:
#                 print("n is a prime number")



# n= int(input("enter the number you want: "))
# for i in range (1,n+1):
#          if(i==1 or i==n):
#                  print("*"*n)
#          else:
#                  print("*", end="")        ***
#                  print(" "*(n-2), end="")  * *
#                  print("*")                ***
        
  


# n= int(input("enter the number you want: "))                   *
# for i in range (1,n+1):                                       ***
#         print(" "* (n-i),end=" ")                            *****
#         print("*"*(2*i-1))




# def avg():
#    a= int(input("enter the number you want"))
#    b= int(input("enter the number you want"))
#    c= int(input("enter the number you want"))
#    avergae= (a+b+c)/3
#    print(avergae)
#    return 2
# a= avg()   


# def goodDay(name,ending):
#     print("Good Day",name)
#     print(ending)
#                           wihtout any return value 

    
# a=goodDay("som","Thanks")
# print(a)

# def getGreeting(name):
#     return f"Good Day {name}"

# msg = getGreeting("Som")
# # print(msg)                      with a return value .....


# def factorial(n):    
#  if(n==1 or n==0):
#   return 1
#  else:
#   return n*factorial(n-1)


# n= int(input("enter the number you want "))
# print(f" the factorial of {n} is: {factorial(n)}")


# def greatest(a,b,c):
#  if (a>b and a>c):
#      return a
#  elif(b>a and b>c):
#     return b
#  elif(c>a and c>b):
#      return c
    
    
# a= int(input("enter the first number"))
# b= int(input("enter the second number"))
# c= int(input("enter the third number"))

# print("greatest number is ", greatest(a,b,c))



# def degree(f):
#    return 5*(f-32)/9


# d= int(input("enter the farenhite degree you want: "))
# print(d)

# def num():
#   print("value is 29")
#   print("value is 845")
#   return 7


# a=num()
# print(a)


# def inc(inch):
#   return inch*2.54

# n=int(input("enter the number you want to coonvert:"))

# print(f"the cm value is {inc(n)}")


#   REMOVING A SINGLE ELEMENT ##

# def remove(p,word):
#   for item in p:
#     p.remove(word)
#     return p
  
# p = [ "Omm ", "Som","MMrunal","mm"]
# print(remove(p,"mm"))

def remove(p,word):
  n=[]
  for item in p:
    if( item == word):
     n.append(item.replace(word,""))
  return n
     
     
p = ["Omm", "Som", "MMrunal", "mm"]
print(remove(p, "mm"))