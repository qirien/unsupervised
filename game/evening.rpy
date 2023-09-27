# Evening Events
# Evening includes chores, homework, video games, reading a book,
label evening_default:
    scene bedroom
    # TODO: Replace with adventure game-style point and click house
    call freetime_menu(2)

    return

label homework:
    scene bedroom
    "I wrote the answers as fast as possible."
    $ stat_change(grades, 2)
    return

label tv:
    scene living
    "I watched a few episodes of a show."
    return

label read:
    scene living
    "I read a few chapters of my book."
    $ stat_change(grades, 1)
    return

label clean:
    scene kitchen
    "I washed my dishes and wiped the crumbs off the counter."
    $ stat_change(house,2)
    return
