# Events where you try to research what happened to Mom to increase your 'research_pts' variable
# TODO: Is there another way to get research_pts or does it need a different next_event algorithm?

label research:
    scene master bedroom day
    $ next_event = get_next_event("research")
    call expression next_event
    $ looked_for_clues = True #you can only do one research per day
    return

label research_random:
    "I rummaged through my mom's stuff, looking for clues. I didn't find any, though."
    $ research_pts += 1
    return

label research0:
    "My mom was missing, and I wasn't sure her work was going to be able to find her."
    "It was up to me."
    "I read the text she had sent me again."
    nvl clear
    # TODO: store this in some way so there's no copy/paste?
    # TODO: Make this a screen of hot spots where the user gets to pick what to investigate?
    # TODO: show picture here, too
    mom_text "Don't know if you'll get this, had to borrow a phone, not everyone has them out here. Yours is only number I have memorized. If work calls, show them my message. Trying to send a pic."
    mom_text "Guess you're not on your phone now; good job, [your_name]. I gotta go, though, so I won't get replies. Text you again when I can."
    you_text "Mom?! Mom, it's [your_name]! Where are you?!"
    mom_text "Извини. я не могу тебе помочь."
    "That response... the letters definitely weren't English. I searched for that phrase..."
    you "Looks like it's... Russian? 'Sorry, I can't help you'."
    you "There's a lot of countries that speak Russian..."

    "I returned to the photo she sent."
    "In the background, I could see grass and rocky hills."
    you "So she's probably near some plains?"
    "I pored over maps and Wikipedia and found a hundred places she could be."
    "I just didn't have enough information."
    $ research_pts += 1
    $ research_next += 1
    return

label research1:
    "time zone and time of day research"
    $ research_pts += 1
    $ research_next += 1
    return

label research2:
    "Looking through her work bag research"
    $ research_pts += 1
    $ research_next += 1
    return

label research3:
    "I remember my mom making me change some setting so my phone didn't save GPS data with pictures."
    "Maybe there was GPS data in the photo she sent me?"
    "Once I thought of it, I couldn't think of anything else until I checked."
    "I saved the photo to my phone, and then looked at the photo's information tags..."
    "Sure enough, there was a GPS location there!"
    "I punched it into the map..."
    you "Kazakhstan?"
    you "They speak Russian and Kazakh... which is sometimes written with Arabic, Cyrillic, or Latin characters?"
    you "Low population density - I guess it's big but not very many people live there?"
    you "Used to be part of the Soviet Union..."
    you "Natural resources include oil and gas..."
    "I spent the rest of the night reading up on Kazakhstan..."

    $ research_pts += 1
    $ research_next += 1
    return
