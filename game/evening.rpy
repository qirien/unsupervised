# Evening Events
# Evening includes chores, homework, video games, reading a book,
label get_event_evening(curr_day):
    scene bedroom
    # TODO: Replace with adventure game-style point and click house
    call freetime_menu(2)

    return

label homework:
    scene bedroom
    "I wrote the answers as fast as possible."
    return

label tv:
    scene living
    "I watched a few episodes of a show."
    return

label read:
    scene living
    "I read a few chapters of my book."
    return

label clean:
    scene kitchen
    "I washed my dishes and wiped the crumbs off the counter."
    return
