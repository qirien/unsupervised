# Plot events that happen on certain days on wakeup


# TODO: show picture here, too
label mom_text0:
    nvl clear
    mom_text "Don't know if you'll get this, had to borrow a phone, not everyone has them out here. Yours is only number I have memorized. If work calls, show them my message. Trying to send a pic."
    mom_text "Guess you're not on your phone now; good job, [your_name]. I gotta go, though, so I won't get replies. Text you again when I can."
    you_text "Mom?! Mom, it's [your_name]! Where are you?!"
    mom_text "Извини. я не могу тебе помочь"  #TODO: validate with Russian speaker 'sorry, I can't help you.'
    nvl clear
    return

label wakeup4:
    "Living on my own wasn't as hard as I thought it would be."
    "But I still missed my mom."
    "I woke up and found a new message from her on my phone."

    call mom_text0

    "I guess she's moved on... "
    "I stared at the picture again. My mom was alive..."

    if met_mark:
        menu:
            "What should I do?"
            "Text coworker":
                "I pulled out my mom's phone again. It was full of notifications but most of them weren't important."
                nvl clear
                you_text "My mom texted me... she borrowed a phone."
                coworker_text "Really?! Where is she? What did she say?"
                you_text "She didn't say... she had to borrow a phone and then she left so I can't text her back. She said she's somewhere where not everyone has phones."
                coworker_text "Really? That narrows it down a little... Thank God she's all right. If anyone could survive being dropped in the middle of nowhere, it's your mom."
                you_text "The middle of nowhere? Where is she?"
                coworker_text "Ahhh, sorry kid, it's classified. We haven't given up on her, though! Let me know if you find out anything else."
                nvl clear
            "Don't text him":
                $ pass
    "I sat there for a few minutes, just thinking about Mom."
    you "Guess I better get ready for school!"
    "I rushed through breakfast and barely made it to school on time."

    return

# On day 6, get another text from Mom.
# TODO: include picture of Mom in front of some Russian street signs?
label wakeup6:
    nvl clear
    "I woke up to a text from a strange number... maybe it was my mom?!"
    mom_text "I borrowed another phone. I'm still here. I tried to call but I guess it's the middle of the night for you."
    mom_text "I'm really in the middle of nowhere... I'm heading home but I might be awhile."
    mom_text "Take care of yourself, and don't be afraid to ask for help!"

    "It was several hours ago... there'd be no point in texting back."
    "Mom was still alive... and thinking about me."
    "I changed my phone to allow calls from random numbers at night, just in case she tried to call again."
    nvl clear
    return

# Finally, a phone call from mom! This ends Act II.
label wakeup10:
    "I woke up in the middle of the night to my phone vibrating."
    "I was confused and picked it up, staring at the screen. Some random international number was calling..."
    "It might be mom!"
    you "Hello?"
    mom "[your_name]? Is it you?!"
    you "Mom!"
    mom "Oh, it's so good to hear your voice!"
    you "Oh, mom..."
    mom "Okay, I don't have much time... I am slowly working my way home, but it's taking a long time. There's no planes out here, no buses, I have no ID or credit cards or money..."
    you "Where are you?"
    mom "I'm in a town... I think it's called Jezkan or Jezgan or something." #TODO: does Zhezqazghan make sense? Coming from mountains, on way to larger city?
    you "Can't your work help you?"
    mom "They are working on it... with the war going on nearby travelling is tricky. I'm trying to get home without mentioning my work, since... well, you know."
    you "No, I don't know! What do you mean?!"
    mom "I can't talk about it right now. But I have reasons, good ones. And I will be home eventually!"
    menu:
        "What should I say?"
        "I need you!":
            $ anxious += 1
            you "But... I need you."
            mom "Oh sweetie... It must be so hard. You could always ask dad for help..."
        "I'm doing fine without you.":
            $ rebellious += 1
            you "I'm doing fine without you."
            mom "I bet you are, my independent child. But if you get stuck, you can ask dad."
        "Don't worry about me.":
            $ independent += 1
            you "Don't worry about me. You just worry about getting home."
            mom "You're just handling everything on your own, aren't you? Well, I suppose dad's there if you need him..."
    you "I'm not asking dad for help unless I have no other choice."
    mom "Just do your best. It'll be enough, and we'll be together soon."
    you "I will. Can I help you somehow?"
    mom "Hmmm... just take care of yourself, and I'll do the rest. There's cash in my sock drawer if you need it."
    mom "I have to go now, though. I'll try to call you again sometime! Goodbye, [your_name]."
    you "Bye, mom..."

    "I waited until she hung up. It was the middle of the night but I was wide awake now."
    "Why would she not want to mention her work? They were the reason she was out there; they should be able to help get her out!"
    "And would she be okay being so close to the war?"
    "My thoughts tumbled over each other like clothes in the dryer."
    "I never did get back to sleep..."

    # TODO: interscene text saying "Act III" or something?

    return
