# Events for the Climbing Club, which leads to better friendship with Tabitha.

# Random generic events
label tabitha_random:
    "I climbed some easy walls and tried some hard bouldering problems."
    "In between sets, I watched Tabitha climb. She made everything look easy."
    $ tabitha_pts += 1
    return

label tabitha0:
    "What's climbing about? Tabitha ignores yoU!"
    $ tabitha_pts += 1
    $ tabitha_next += 1
    return

label tabitha_final:
    "The big meet was over, so I just climbed for fun."
    return
