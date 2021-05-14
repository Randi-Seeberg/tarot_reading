from focus_areas import focus_areas, add_focus_area

#Prints dict focus_areas [number:fa]
def print_focus_areas():
    print("\n")
    for key in focus_areas:
        print(str(key) +"   "+ focus_areas[key]+"\n")

def choose_focus_area():
    input=("Which area would you like to focus on? Type R for Relationships, C for Career, or P for Personal development.")
    return input
    #So that this can take number and retrieve fa

def welcome():
    print("\nWelcome to Mme Nugget's tarot reading!")
    print("\nYour reading will focus on one of three important areas of your life: \n")
    print_focus_areas()
    choose_focus_area()


    

