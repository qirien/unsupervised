# Define variables and run init code

# CHARACTERS
define you = Character("your_name", dynamic=True)
define ryan = Character("Ryan")
define emir = Character("Emir")
define tabitha = Character("Tabitha")
define nina = Character("Nina")
define math_teacher = Character("Mr. Factor")
define note = Character(kind=nvl)

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

# The game starts here.

label start:


    scene bg room

    call act1
    call act2
    call act3
    call act4
    call act5

    return
