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

# TODO: Make this a screen of hot spots where the user gets to pick what to investigate?
label research0:
    "My mom was missing, and I wasn't sure her work was going to be able to find her."
    "It was up to me."
    "I read the text she had sent me again."
    call mom_text0
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

# Turn this into hot spots you click on to get different text
label research1:
    "I stared at the photo my mom had sent. She didn't look sad or hurt."
    "Just worn-out, like she'd been traveling a lot."
    # if you click the "Ask Me!" button
    you "Hey phone, where is my mom?"
    "Phone" "Sorry, I don't have any information about that. Try saying 'play some music' or 'tell me a joke'."
    "It was worth a try."
    # clock app
    "I opened up the clock app and found the world map, where it showed the current time at different places around the world."
    "What time was it where she was?"
    "Wait... I had some clues about that!"
    you "She texted me at 7:30am my time..."
    "I looked at the picture again. Obviously it was day time where she was, but was it morning? Or afternoon?"
    "There were some long shadows, so it wasn't noon."
    "I noticed a half moon in the sky in the background. Was the moon up in the morning or evening? Was that the same all over the world?"
    "Now I had to research the moon..."
    # Wikipedia simple moon page?

    you "Hey phone, what was the phase of the moon on the date this picture was taken?"
    "Phone" "First Quarter, 56\% illuminated"
    "'In the first quarter, during the afternoon, our natural satellite can be seen rising in the eastern sky.'"
    you "So when it was morning here, it was afternoon there!"
    "I looked at my world time map again."
    you "That means... she must be somewhere between Europe and Asia. Or maybe East Africa...?"
    you "Russian-speaking, so probably not Africa."
    "That was still a huge part of the Earth. But the more I found out, the closer I felt to her."
    # TODO: Have a map of the world where you slowly narrow down where she might be

    $ research_pts += 1
    $ research_next += 1
    return

label research2:
    "I looked around my mom's room, wondering if she had left anything that could tell me where she was or what she was doing."
    you "Most of her stuff is probably at work..."
    "I checked her email... but it wasn't her work email; just her personal email."
    "Sales, reminders, receipts, stuff for school... uh-oh."
    "There was an email from one of my teachers!"
    # changes based on grades

    nvl clear
    math_teacher_text "Hey, I noticed you hadn't returned your parent feedback form and just wanted to send a reminder to do that if you can."
    if (good_stat(grades)):
        math_teacher_text "It's a pleasure to have [your_name] in my class. She often helps other students and always has interesting things to say."
    else:
        math_teacher_text "[your_name] is trying in class, but she hasn't been doing her homework and her grades are starting to suffer."

    "Parent feedback form?? Well, that was just one of many things that my mom wasn't doing right now."

    "I searched her purse."
    "Lip balm, tissues, tampons, breath mints... boring stuff."
    "But there was a small pad of paper."
    "It was blank, but I could see some indentations from something she had written, then torn the page off. If I looked closely, I could almost make out words... but not quite."
    "One of my detective books had something about this!"
    "I could rub over the paper with pencil and the words should show up!"
    "I ran and grabbed a pencil."
    "Shading lightly, but carefully, I could read what she had written..."
    # TODO: Have a pic for this
    nvl clear
    note "Field Test Checklist"
    note "No metal/electronics!! (magnetic field resonance)"
    note "Check oscillation tolerances"
    note "Phase variance increasing over time?"
    note "Drop site team check"
    note "Take [your_name] out for ice cream!"
    nvl clear

    you "We never did go out for ice cream..."
    "I wasn't sure what all that meant, but it sounded like parts of the experiment she was doing for work."
    "But what kind of experiment sends someone all the way around the world??"
    "Time to research teleportation, I guess..."

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

label research4:


    $ research_pts += 1
    $ research_next += 1
    return
