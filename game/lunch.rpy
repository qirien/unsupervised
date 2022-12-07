# Lunch events
# 50% of the time there's no event, just flavor text.
# The other 50% it will ask who you want to hang out with.

label get_event_lunch(curr_day):
    scene cafeteria
    "I ate my lunch and wandered around, just like I had for the past [curr_day] school days. It felt good to be outside in the sunshine."
    return




label lunch2:
    scene school
    "The morning passed by quickly."


    scene cafeteria
    "As I waited in line for my lunch, I noticed that all the clubs and teams had setup booths around the cafeteria to try to get people to join."
    show emir happy at center
    "Emir got in line next to me."
    if (emir_pts >= 2):
        emir "Too bad there's no fartball club! You could be the president."
        you "You'd be the founding father. The George Washington of fartball."
        emir "Ha ha! Yeah!"
    "We both looked around the room for a minute."
    emir "Cross country? What's that, like going on road trips?"
    you "I think it's running? Long distances?"
    emir "Oh, that makes more sense. Too bad it's not like a motorcycle gang or something!"
    you "What's the Maker's Club?"
    emir "Oh, I have a class in the Makerspace. It's like a room with tools and materials and you can make things. Sometimes they have robots and 3D printers and stuff. So Maker's Club is making things there."
    "We got our food and Emir sat down at an empty table. I looked around, but I didn't see anyone else I knew."
