from questions import questions, add_question
from cards import cards
import random

def welcome():
    print("\nWelcome to Mme Nugget's tarot reading!")

#Prints dict questions [number:q]
def show_questions():
    for key in questions:
        print(str(key) +"   "+ questions[key]+"\n")

def choose_question():
    choice=int(input("Please type the number of your chosen question: "))
    if choice in questions.keys():
        print("\nYou have chosen the question: " + questions[choice])
        print("\nInteresting choice!")    
        return(choice)
    else:
        if choice not in questions.keys():
            print("This is not a valid number. Please try again.")
            choose_question()  

def pick_random_card():
    print("\nNow, let me shuffle the cards for you.\n")
    print("\nThe cards are shuffled. I will now turn the top card of the deck for your reading.")
    random_card = random.choice(list(cards.items()))
    print("\nYour card is: " + random_card[0] + "\n")
    return random_card

def reading():
    print("\nYour reading will centre on one of {} important questions about your life right now: \n".format(len(questions)))
    show_questions()
    choice=choose_question()    
    

pick_random_card()

