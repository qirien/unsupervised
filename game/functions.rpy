label find_class(desired_room):
    $ picked_room = ""
    while (picked_room != desired_room):
        call screen school_map
        $ picked_room = _return
        if (picked_room != desired_room):
            $ random_response = renpy.random.choice(
            ["I tried to follow the map, but ended up at [picked_room] instead. Guess I'll have to try again.",
            "Whoa, how did I end up at [picked_room]? I looked at my map again.",
            "Well, I wasn't at [desired_room], but at least I found out where [picked_room] was."
            ])
            $ renpy.say(None, random_response)
    return

label adventure_mode(start_room):
    $ current_room = start_room
    $ previous_room = start_room

    #$ renpy.show_screen(current_room + "Screen")
    window auto hide

    $ in_room = True
    $ renpy.call_screen(current_room + "Screen")
    return

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


# Utility functions and variables used elsewhere
init -100:
    transform highlight_imagebutton():
        on hover:
            additive 0.2
        on idle:
            additive 0.0

    transform alpha_imagebutton():
        on start:
            alpha 0.6
        on idle:
            alpha 0.6
        on hover:
            alpha 1.0
