questions={
1:"What will be the best career moves for me to take in the near future?", 
2:"What steps can I take to improve the quality of my relationships with other people?", 
3:"What would you advise me to focus on in my efforts for personal development?"
}

def add_question(new_value):
    key = len(questions) + 1
    questions[key] = new_value
    print(questions)