questions={1:"Question1", 2:"Question2", 3:"Question3"}

def add_question(new_value):
    key = len(questions) + 1
    questions[key] = new_value
    return questions