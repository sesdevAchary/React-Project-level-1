# 🎯 Objective of the Script
# The main purpose of quiz_maker.py is to create a simple CLI-based quiz management system that supports:

# User registration and login

# Role-based access: Admins can create quizzes, regular users can take quizzes

# Quiz creation with multiple question types (mcq, true/false, short answer)

# Storing and loading data (users and quizzes) using JSON files


import json #Allows reading and writing of user/quiz data in JSON format.
import os   #Used to check if a file exists (os.path.exists()).
import uuid  #Used to generate unique IDs for each question (uuid.uuid4()).


class user:
    def __init__(self , username,password,is_admin=false): #constructor method#
        self.username=username
        self.password=password
        self.is_admin=is_admin  #is_admin helps separate regular users from admins.
        
    def to_dict(self):  #Converts the User object to a dictionary for easy storage (e.g., in a JSON file).
        return{
            "username":self.username,
            "password":self.password,
            "is_admin":self.is_admin
            #Returns a dictionary with all user attributes.
            
        }
        
    @staticmethod   #Can be called without creating a User objec
    def from_dict(data):  #Takes a dictionary (data) and turns it into a User object.
        return user(data['username'],data['password'],data['is_admin'])
    #Creates and returns a new User instance using data from the dictionary.
    


