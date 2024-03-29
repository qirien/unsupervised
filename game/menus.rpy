# This gets called when you have free time.
# It changes to adventure mode and lets you do a certain number of things.
# TODO: Should this allow for smaller events, maybe giving a certain number of hours and each event takes a fraction of an hour?
label freetime_menu(menu_count=1):
    $ picked_room = "Hallway"
    while (menu_count > 0):
        $ print("Starting ADV mode on: " + picked_room + "  Count: " + str(menu_count))
        call adventure_mode(picked_room)
        $ picked_room = current_room
        $ menu_count = menu_count-1
return

label textfreetime_menu(menu_count=1):
    while (menu_count > 0):
        # TODO: Add more options, randomness here
        menu:
            "What should I do?"
            "Clean the house":
                "I took some time to clean my room."
                $ menu_count = menu_count -1
            "Do homework":
                "I worked on my school assignments."
                $ menu_count = menu_count -1
            "Play games":
                "I logged on to Virtopia."
                if (menu_count > 1):
                    "Before I knew it, several hours had passed."
                else:
                    "I had time to add a room onto my house and try my friend's new maze level."
                $ menu_count = 0
            "Read a book":
                "I read a few chapters in my novel."
                $ menu_count = menu_count -1
            "Watch something":
                "I started watching a new series."
                if (menu_count > 1):
                    "Before I knew it, several hours had passed."
                else:
                    "I had time to watch two episodes."
                $ menu_count = 0
            "Search for Mom" if (day > 2):
                "I looked around for clues about where Mom could have gone."
                $ menu_count = menu_count -1

    return

# Cooking menu
# TODO: have different options depending on how late/hungry
# TODO: have some random options
# TODO: If researched cooking in spare time, allow cooking more advanced meals
label meal_menu():
    scene kitchen
    menu:
        "What should I eat?"
        "Cook scrambled eggs.":
            "Cooking eggs is pretty easy. Heat up the pan, crack the eggs in a bowl, whisk them around, add some salt and pepper, and cook them up."
            "And eggs are healthy, so that's good, too."
        "Make pancakes":
            "We had a huge box of pancake mix, so making pancakes was pretty easy. I poured syrup all over them... yum!"
        "Eat healthy snacks.":
            "I ate some carrots and an apple and some crackers and cheese. Easy."
        "Eat junk food.":
            "I pulled out a bag of chips and some fruit snacks. My mom was probably saving them for a special occasion, but too bad. She wasn't here."
            $ health_change(-1)
        "Order pizza." if ((day > 2) and (money >= PIZZA_COST)): # TODO: Disable if you haven't found mom's phone yet or you don't have money
            "I used my mom's phone to order a pizza. Thirty minutes later, it arrived. I ate half of it myself and put the other half in the fridge for later."
            $ money -= PIZZA_COST

    return
