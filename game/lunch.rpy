# Lunch events

# Function for if nothing else is happening and you can choose who to sit with
label lunch_default:
    scene cafeteria
    "I looked around the cafeteria and saw a few people I had met."
    # TODO: Add functions for these and different events
    menu:
        "Who should I sit with?"
        "Nina" if met_nina:
            "I plopped down next to Nina and a bunch of kids from drama club."
        "Emir":
            "Emir waved me over to his table and I sat down."
        "Calvin" if met_calvin:
            "I saw Calvin take his food out the door. He was probably headed to the Makerspace, so I followed him."
        "Tabitha" if met_tabitha:
            "Tabitha was sitting alone as usual until I sat down across from her."
    return


label lunch_a:
    scene cafeteria
    
    "I ate my lunch and wandered around, watching people and thinking. It felt good to be outside in the sunshine."
    return

label lunch_b:
    scene cafeteria
    "It was raining, so I decided to eat inside."
    return

label lunch2:
    scene cafeteria
    "As I waited in line for my lunch, I noticed that all the clubs and teams had setup booths around the cafeteria to try to get people to join."
    show emir happy at center
    "Emir got in line next to me."
    if (emir_pts >= 2):
        emir "Too bad there's no fartball club! You could be the president."
        you "You'd be the founding father. The George Washington of fartball."
        emir "Ha ha! More like the 'farting father'."
    "We both looked around the room for a minute."
    emir "Cross country? What's that, like going on road trips?"
    you "I think it's running? Long distances?"
    emir "Oh, that makes more sense. Too bad it's not like a motorcycle gang or something!"
    you "What's the Maker's Club?"
    emir "Oh, I have a class in the Makerspace. It's like a room with tools and materials and you can make things. Sometimes they have robots and 3D printers and stuff. So Maker's Club is making things there."
    "We got our food and Emir sat down at an empty table. I looked around, but I didn't see anyone else I knew."


    return

