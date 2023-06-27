# Define variables and run init code

# CHARACTERS
define you = Character("your_name", dynamic=True, who_color="#59c3cf")
define ryan = Character("Ryan")
define emir = Character("Emir", image="emir", who_color="#dac96c")
define tabitha = Character("Tabitha", image="tabitha", who_color="#ee22aa")
define nina = Character("Nina", image="nina", who_color="#eedd11")
define math_teacher = Character("Mr. Factor")
define drama_teacher = Character("Ms. Hicks")
define note = Character(kind=nvl)
define coworker_text = Character("Mark Yao", kind=nvl)
define you_text = Character("your_name", kind=nvl, dynamic=True)
define mom_text = Character("Unknown Number", kind=nvl)
define quiz = Character(kind=nvl)

# VARIABLES FOR STATS
default health = 100
default stress = 0
default grades = 0
default house = 100
default research_pts = 0
default research_next = 0
default money = 2000
default looked_for_clues = False

# VARIABLES FOR MC
default your_name = "Me"
default independent = 0
default anxious = 0
default rebellious = 0
default she_he = "she"
default she_he_is = "she is"
default she_he_s = "s"
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

default nina_next = 0
default calvin_next = 0
default emir_next = 0
default tabitha_next = 0
default magicghoulbus_next = 0

default met_nina = False
default met_calvin = False
default met_emir = True
default met_tabitha = False
default met_magicghoulbus = False
default met_mark = False

# VARIABLES FOR SCHEDULE
default day = 1
default clubs = []
define MAX_DAYS = 30
default time_block = 0
define time_blocks = ["morning", "lunch", "afternoon", "afterschool", "evening", "night"] #should evening and night be the same?
define time_blocks_pretty = ["Morning", "Lunch", "Afternoon", "After School", "Evening", "Night"]
define MAX_TIMEBLOCKS = 6

# VARIABLES FOR ADVENTURE MODE
default current_room = "Hallway"
default previous_room = ""
default move_count = 0
default in_room = False

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

    # INTRO is special
    call act1
    
    $ day = 2
    while (day <= MAX_DAYS):
        # Reset for a new day
        $ looked_for_clues = False
        # If we have a wakeup event, do that first
        $ next_label = "wakeup" + str(day)
        if (renpy.has_label(next_label)):
            call expression next_label

        # Weekend Events
        # IF event for that day #, do that. ELSE choice of home/park/shopping activities
        if (is_weekend(day)):
            "Ahhh, the weekend..."
            $ next_label = "weekend" + str(day)
            if (renpy.has_label(next_label)):
                call expression next_label
            else:
                "I slept in and had time to do a few things."
                call freetime_menu(3)
                call meal_menu

        # Weekday Events / School
        else:            
            $ time_block = 0
            # Morning, Lunch, Afternoon, After School, Evening, Night
            while (time_block < MAX_TIMEBLOCKS):
                $ next_label = time_blocks[time_block] + str(day)
                if (renpy.has_label(next_label)):
                    call expression next_label
                else: 
                    call expression "get_event_" + time_blocks[time_block] pass (day)
                $ time_block += 1
        $ day = day + 1
    
    # THE END
    #call ending
    #call credits

    return
