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
#                  print("*", end="")
#                  print(" "*(n-2), end="")
#                  print("*")
        
  


n= int(input("enter the number you want: "))
for i in range (1,n+1):
        print(" "* (n-i),end=" ")
        print("*"*(2*i-1))
