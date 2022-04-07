# Define variables and run init code

# CHARACTERS
define you = Character("your_name", dynamic=True)
define ryan = Character("Ryan")
define emir = Character("Emir", image="emir", who_color="#dac96c")
define tabitha = Character("Tabitha")
define nina = Character("Nina")
define math_teacher = Character("Mr. Factor")
define note = Character(kind=nvl)
define coworker_text = Character("Mark Yao", kind=nvl)
define you_text = Character("your_name", kind=nvl, dynamic=True)

# VARIABLES FOR STATS
default health = 100
default stress = 0
default grades = 0
default house = 100
default clues = 0
default money = 2000

# VARIABLES FOR MC
default your_name = "You"
default independent = 0
default anxious = 0
default rebellious = 0
default she_he = "she"
default her_him = "her"
default her_his = "her"
default hobby = "draw"
default favorite_food = "pizza"
default hated_action = "are hypocritical"


# VARIABLES FOR FRIENDSHIPS
default nina_pts = 0
default calvin_pts = 0
default emir_pts = 0
default tabitha_pts = 0
default magicghoulbus_pts = 0

# VARIABLES FOR SCHEDULE
default day = 1
default clubs = []

# VARIABLES FOR DISPLAY
transform midleft:
    xpos 0.35 xanchor 0.5 ypos 1.0 yanchor 1.0
transform midright:
    xpos 0.65 xanchor 0.5 ypos 1.0 yanchor 1.0
transform quarterleft:
    xpos 0.22 xanchor 0.5 ypos 1.0 yanchor 1.0
transform quarterright:
    xpos 0.78 xanchor 0.5 ypos 1.0 yanchor 1.0

# The game starts here.

label start:
    scene bg room

    $ act = 1
    while (act <= 5):
        call expression "act" + str(act)
        $ act = act + 1

    # Daily Loop (usually random, unless there exists an event for that day)
    # Morning class events (advisory, gym, math, social studies)
    # Lunch events/choices (which friend to hang out with)
    # Afternoon class events (English, science, technology/art?)
    # After school events/choices (M/W clubs or T/TH clubs or F hangout event?)
    # Evening events/choices

    return
