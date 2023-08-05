# Events for when you choose to play video games

label videogames:
    $ next_event = get_next_event("magicghoulbus")
    call expression next_event
    return

label magicghoulbus_random:
    if (met_magicghoulbus):
        "I logged on and talked to MagicGhoulBus while we played a few levels."
    else:
        "I logged on and played a few levels."
    $ magicghoulbus_pts += 1
    return

# Who is MagicGhoulBus?
label magicghoulbus0:
    "They were having a back to school event with school-themed levels."
    "I tried the school bus race, a books in the locker puzzle level that was kind of like tetris, and a level with a tricky jumping puzzle to get on the school's roof."
    "I used to have the #1 time on the school bus race... but someone beat me. I had to see who."
    "MagicGhoulBus? I didn't recognize the name; must be someone new. They weren't online now, though, so I didn't get a chance to meet them."

    $ magicghoulbus_next += 1
    return

# You meet them when you finally beat their time on the school bus race. You talk, but they have to log off
label magicghoulbus1:
    "You meet them when you finally beat their time on the school bus race. You talk, but they have to log off"
    "Someone claims you are cheating but they defend you."

    $ magicghoulbus_next += 1
    return

# They say it's getting late and you find out they are in a different country
label magicghoulbus2:
    "They say it's getting late and you find out they are in a different country"

    $ magicghoulbus_next += 1
    return

# Someone is interested in them online and they ask your opinion
label magicghoulbus3:
    "Someone is interested in them online and they ask your opinion"

    $ magicghoulbus_next += 1
    return

# You decide to build a level together
label magicghoulbus4:
    "You decide to build a level together for a contest."

    $ magicghoulbus_next += 1
    return

# You work on the level together. You disagree and have to compromise.
label magicghoulbus5:
    "You work on the level together. You disagree and have to compromise."

    $ magicghoulbus_next += 1
    return

#You finish your level and other people think it's too hard. But you had fun!
label magicghoulbus6:
    "You finish your level and other people think it's too hard. But you had fun!"

    $ magicghoulbus_next += 1
    return

# End event.
label magicghoulbus_final:
    "You play a few levels with MagicGhoulBus."
    return
