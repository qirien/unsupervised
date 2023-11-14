# Evening Events
# Evening includes chores, homework, video games, reading a book,
label evening_default:
    scene bedroom day
    # TODO: Replace with adventure game-style point and click house
    call freetime_menu(2)

    return

label homework:
    scene bedroom day
    $ random_response = renpy.random.choice(
    ["I wrote the answers to my homework as fast as possible.",
     "I read a section in the textbook and took some notes.",
    "I got some work done on a presentation.",
    "I studied for a test I had coming up.",
    "I watched a video and answered the questions about it."])
    $ renpy.say(None, random_response)
    $ grades_change(2)
    return

label tv:
    scene living
    "I watched a few episodes of a show."
    return

label read:
    scene living
    "I got cozy and read a few chapters of my book."
    $ grades_change(1)
    return

label clean:
    scene kitchen
    "I washed my dishes and wiped the crumbs off the counter."
    $ grades_change(2)
    return
