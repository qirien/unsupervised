init python:
    def dayofweek(day):
        if (day % 7 == 1):
            return "Monday"
        elif (day % 7 == 2):
            return "Tuesday"
        elif (day % 7 == 3):
            return "Wednesday"
        elif (day % 7 == 4):
            return "Thursday"
        elif (day % 7 == 5):
            return "Friday"
        elif (day % 7 == 6):
            return "Saturday"
        elif (day % 7 == 0):
            return "Sunday"

    def is_weekend(day):
        dayname = dayofweek(day)
        if (dayname == "Saturday") or (dayname == "Sunday"):
            return True 
        return False

    def random_float():
        return renpy.random.random()
    
    def random_int(min, max):
        return renpy.random.randint(min, max)

    def get_your_adjective():
        if (rebellious >= anxious >= independent):
            return "rebellious"
        elif (anxious >= rebellious >= independent):
            return "anxious"
        else:
            return "independent"