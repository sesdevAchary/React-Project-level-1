## PERSONAL ASSISTANT CONSOLE APP....

import random   #Used to randomly pick a motivational quote.
import datetime 

quotes=[
    "Keep going, you're doing great!",
    "Stay positive and work hard.",
    "Success is a journey, not a destination.",
    "Believe in yourself!",
    "Every day is a second chance."
]


def greeet_user():
    name =print(input("👋 Hello! What's your name?"))
    print(f"Welcome ,{name} ! I am your personal assistant ")
    return name
