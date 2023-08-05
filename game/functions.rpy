label find_class(desired_room):
    $ picked_room = ""
    while (picked_room != desired_room):
        call screen school_map
        $ picked_room = _return
        if (picked_room != desired_room):
            $ random_response = renpy.random.choice(
            ["I tried to follow the map, but ended up at [picked_room] instead. Guess I'll have to try again.",
            "Whoa, how did I end up at [picked_room]? I looked at my map again.",
            "Well, I wasn't at [desired_room], but at least I found out where [picked_room] was.",
            "This wasn't [desired_room]. Ugh."
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



# If you have enough points to move on to the next plot event, great.
# Otherwise, you get a generic event.
init -100:
    python:
        def get_next_event(event_type):
            next_event_number = eval(event_type + "_next")
            next_unseen_event = event_type + str(next_event_number)
            # if we went past the number of events written, just go to the final one.
            if (not renpy.has_label(next_unseen_event)):
                next_unseen_event = event_type + "_final"
                return next_unseen_event

            # Do we have enough points for this?
            points = eval(event_type + "_pts")
            renpy.notify("Pts:" + str(points) + "  i:" + str(next_event_number) + "  next_label=" + str(next_unseen_event))
            if points >= (2*next_event_number): # TODO adjust this calculation
                if (renpy.has_label(next_unseen_event)):
                    return next_unseen_event

            # No better event, just use the random one
            next_unseen_event = event_type + "_random"
            return next_unseen_event


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
