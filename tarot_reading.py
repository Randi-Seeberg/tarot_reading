from questions import questions, add_question
from random import random

def welcome():
    print("\nWelcome to Mme Nugget's tarot reading!")

#Prints dict questions [number:q]
def print_questions():
    for key in questions:
        print(str(key) +"   "+ questions[key]+"\n")

def choose_question():
    choice=int(input("Please type the number of your chosen question: "))
    if choice in questions.keys():
        return(choice)
    else:
        if choice not in questions.keys():
            print("This is not a valid number. Please try again.")
            choose_question()    
    
def reading():
    print("\nYour reading will centre on one of {} important questions about your life right now: \n".format(len(questions)))
    print_questions()
    choice=choose_question()
    print("\nYou have chosen the question: " + questions[choice])
    print("Interesting choice! Now let me shuffle the deck and pick a card for your reading.\n")    

reading()
