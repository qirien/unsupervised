# Events for the Cross Country Club, which leads to better friendship with Emir.

# Random generic events
label emir_random:
    "I ran and ran and ran."
    "I tried to keep up with Emir but he was too fast."
    $ emir_pts += 1
    return

label emir1:
    "What is cross country?"
    $ emir_pts += 1
    $ emir_next += 1
    return

label emir_final:
    "Even though the big meet was over, some of us still met to run and hang out."
    "It felt good to run and exercise with friends."
    return
