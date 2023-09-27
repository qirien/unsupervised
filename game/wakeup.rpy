# Plot events that happen on certain days on wakeup

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

