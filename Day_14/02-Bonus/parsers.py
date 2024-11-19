def parse(feet_inches_arg):
    """ Return a dictionary with the feet and inches """
    parts = feet_inches_arg.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}