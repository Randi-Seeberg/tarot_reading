focus_areas={1:"Relationships", 2:"Career", 3:"Personal development"}

def add_focus_area(new_value):
    key = len(focus_areas) + 1
    focus_areas[key] = new_value
    return focus_areas