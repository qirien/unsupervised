# Plot events that happen on certain days on wakeup

label wakeup4:
    "Living on my own wasn't as hard as I thought it would be."
    "But I still missed my mom."
    "I woke up and found a new message from her on my phone."

    nvl clear
    mom_text "Don't know if you'll get this, had to borrow a phone, not everyone has them out here. Yours is only number I have memorized. If work calls, show them my message. Trying to send a pic."
    mom_text "Guess you're not on your phone now; good job, [your_name]. I gotta go, though, so I won't get replies. Text you again when I can."
    you_text "Mom?! Mom, it's [your_name]! Where are you?!"
    mom_text "Извини. я не могу тебе помочь"  #TODO: validate with Russian speaker 'sorry, I can't help you.'
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

