from questions import questions, add_question
from random import random

#Prints dict questions [number:q]
def print_questions():
    print("\n")
    for key in questions:
        print(str(key) +"   "+ questions[key]+"\n")

def choose_question():
    choice=input("Please type the number of your chosen question.")
    if input not in range(len(questions)):
        print("This is not a valid number. Please try again")
        choose_question()
    return choice
    
def welcome():
    print("\nWelcome to Mme Nugget's tarot reading!")
    
def reading():
    print("\nYour reading will centre on one of {} important questions about your life right now: \n".format())
    print_focus_areas()
    choice=choose_question()
    print("Interesting choice! Now your digital destiny plugin will shuffle the cards and .")    

print(range(len(questions)))