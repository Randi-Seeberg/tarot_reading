from questions import questions
from cards import cards
import random

def welcome():
    print("\nWelcome to Mme Nugget's Tarot Reading!")
    return

def goodbye():
    print("\nThank you for visiting Mme Nugget's Tarot Reading. I hope to see you again some other time!")
    return

def show_questions():
    print("\nYour reading will centre on one of {} important questions about your life right now: \n".format(len(questions)))
    for key in questions:
        print(str(key) +"   "+ questions[key]+"\n")
    return

def choose_question():
    choice = input("Please type the number of your chosen question: ")
    try:
        question_choice=int(choice)
    except:
        print("This is not a valid number. Please try again.")
        return choose_question()

    if question_choice in questions.keys():
        print("\nYou have chosen the question: " + questions[question_choice])
        print("\nInteresting choice!")    
        return question_choice
    else:
        print("This is not a valid number. Please try again.")
        return choose_question()
    
def pick_random_card():
    print("\nLet me shuffle the cards for you.")
    print("\nI will now turn the top card of the deck for your reading.")
    random_card = random.choice(list(cards.items()))
    print("\nYour card is: " + random_card[0])
    return random_card

def print_reading(question, card):
    print("\nThis card has much to say in relation to your question: " + questions[int(question)])
    print("\n" + card[1][int(question) - 1])

def try_again():
    retry = input("\nWould you like to try another reading? Please type 'y' for yes or 'n' for no: ")
    if retry == "y":
        reading()
    elif retry == "n":
        pass
    else:
        print("\nThis is not a valid input. Please try again.")
        try_again()

def reading():
    show_questions()
    question_choice = choose_question()    
    random_card = pick_random_card()
    print_reading(question_choice, random_card)
    try_again()
    
def tarot_reading():
    welcome()
    reading()
    goodbye()

tarot_reading()