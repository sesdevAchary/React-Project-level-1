# 🎯 Objective of the Script
# The main purpose of quiz_maker.py is to create a simple CLI-based quiz management system that supports:

# User registration and login

# Role-based access: Admins can create quizzes, regular users can take quizzes

# Quiz creation with multiple question types (mcq, true/false, short answer)

# Storing and loading data (users and quizzes) using JSON files


import json #Allows reading and writing of user/quiz data in JSON format.
import os   #Used to check if a file exists (os.path.exists()).
import uuid  #Used to generate unique IDs for each question (uuid.uuid4()).


# ========== MODELS ==========#
class user:
    def __init__(self , username,password,is_admin=false): #constructor method#
        self.username=username
        self.password=password
        self.is_admin=is_admin  #is_admin helps separate regular users from admins.
        
    def to_dict(self):  #Converts the User object to a dictionary for easy storage (in a JSON file).
        return{
            "username":self.username,
            "password":self.password,
            "is_admin":self.is_admin
            #Returns a dictionary with all user attributes.
            
        }
        
    @staticmethod   #Can be called without creating a User object
    def from_dict(data):  #Takes a dictionary (data) and turns it into a User object.
        return user(data['username'],data['password'],data['is_admin'])
    #Creates and returns a new User instance using data from the dictionary.
    
    
    class Question:
        def __init__(self,prompt,options,answer,q_types="mcq"):  #Constructor method for Question.   
            self.id= str(uiduuid4()) #Generates a unique ID for each question using uuid4() and converts it to a string.
            self.prompt=prompt  # (question text), "What is 2+2?",
            self.options=options
            self.answer=answer
            self.q_types=q_types
            
        def to_dict(self): #Converts the Question object to a dictionary.
         return {    #Returns a dictionary containing all question data.
            "id":self.id,
            "prompt":self.prompt,
            "options":self.options,
            "answer":self.answer,
            "q_type":self.q_types
            
            
          }
         @staticmethod
         def from_dict(data):     #Recreates a Question from saved data (used in load_quizzes()).
           return Question(data['prompt'],data['options'],data['answer'],data['q_type'])
         
    class Quiz:
        def __init__(self,title,question,created_by):
          #Assigns inputs to object attributes.
          self.title=title
          self.question=question
          self.created_by=created_by
         
        def to_dict(self):
            return{
                "title":self.title,
                "question":[q.to_dict() for q in self.question], #convert each q to self dictionary
                "created_by":self.created_by
            }
        @staticmethod
        def from_dict(data):
            quesitons = [Question.from_dict(q) for q in data['quesitons']]
            return Quiz(data['title'],questions,data['created_by'])
     
      
        
        
# ========== FILE OPERATIONS ==========#

USER_FILE='users.json'  #✅ Capital letters are a naming convention for constants in Python.(e.g.-PI = 3.14)
QUIZ_FILE='quizes.json'
# plain text files formatted in JSON.filenames for storing users and quizzes


def load_users():
    if not os.path.exists(USER_FILE):
     return[]
    with open(USER_FILE,'r') as f:
        return [user.from_dict(u) for u in json.load(f)] # refer the notes

def save_users(users):
    with open(USER_FILE,'w') as f:
        json.dump([u.to_dict() for u in users],f, indent=4)
        #json.dump() writes the list of dictionaries to the file.
        
def load_quizzes():
    if not os.path.exists(QUIZ_FILE):
        return []
    with open('QUIZ_FILE','r') as f:
        return[Quiz.from_dict(q) for q in json.load(f)]
def save_quizzes(quizzes):
     with open(QUIZ_FILE, 'w') as f:
        json.dump([q.to_dict() for q in quizzes], f, indent=4)
        
        
        
        function ScrollToTop() {
  const scroll = () => window.scrollTo({ top: 0, behavior: "smooth" });
  return <button onClick={scroll}>Scroll to Top</button>;
}
function Countdown({ seconds }) {
  const [time, setTime] = useState(seconds);

  useEffect(() => {
    if (time <= 0) return;
    const timer = setTimeout(() => setTime(time - 1), 1000);
    return () => clearTimeout(timer);
  }, [time]);

  return <p>{time > 0 ? time : "Time's up!"}</p>;
}

    








