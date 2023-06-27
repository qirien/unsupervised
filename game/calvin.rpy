# Events for the Makerspace Club, which leads to better friendship with Calvin.

# Random generic events
label calvin_random:
    "I hung out at the Makerspace and worked on my project."
    $ calvin_pts += 1
    return

label calvin1:
    "What is the Makerspace? Who is Calvin?"
    $ calvin_pts += 1
    $ calvin_next += 1

label calvin_final:
    "I didn't really want to start a new project, but I went to the Makerspace anyway to help out other people."
    return
