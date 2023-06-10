# Events for the Drama Club, which leads to better friendship with Nina.

# First visit to drama club
label nina1:
    "I wasn't sure what to expect at Drama Club."
    "Reciting Shakespeare? Belting out Disney songs? Acting out tragic deaths from zombie attacks?"
    "The Drama teacher had us all play a name game first."
    drama_teacher "I'll start. My name is Ms. Hicks, and my gesture is this--"
    "She pretended to hold up a book and turn a page."
    drama_teacher "You repeat all the ones before you, and then do yours!"
    nina "OK! That's Ms. Hicks-"
    "She pretended to read a book."
    nina "And I'm Nina and my gesture is fireworks!"
    "She made little bursting motions with her hands, complete with sound effects."
    menu:
        "It's my turn..."
        "That's Nina...":
            you "That's Nina..."
            nina "Hey! You forgot Ms. Hicks!"
            you "Sorry, that's Ms. Hicks..."
        "That's Ms. Hicks...":
            you "That's Ms. Hicks..."
        "That's Emir...":
            you "That's Emir..."
            nina "What?! Who's Emir? Start with Ms. Hicks!"
            you "Sorry, that's Ms. Hicks..."
        "I don't remember.":
            you "Sorry, I don't remember."
            nina "Start with Ms. Hicks."
            you "That's Ms. Hicks..."
    "I pretended to read a book."
    menu:
        "And next comes..."
        "That's Tabitha...":
            you "That's... Tabitha?"
            nina "No, I'm Nina! Short for Marina!"
            you "Sorry, Nina..."
        "That's Ryan...":
            you "That's... Ryan?"
            nina "Ha! No, I'm Nina! Nina Nina Nina!"
            you "Sorry, Nina..."
        "That's Nina...":
            you "That's... Nina."
            $ nina_pts += 1
        "I don't remember.":
            you "...I forgot your name already..."
            nina "It's Nina, like KNEE and then NAH! Because really, knees aren't that cool!"
            you "Okay, Nina..."
    "I did some little fireworks with my hands."
    you "And I'm [your_name]."
    menu:
        "What gesture should I do?"
        "Butterfly hands":
            "I put my hands together and flapped them like butterfly wings."
        "Muscle pose":
            "I flexed my arm to show off my muscles."
        "Binocular hands":
            "I made my hands into circles and put them up to my eyes like binoculars."
        "Scissor hands":
            "I made a V with my two fingers and opened and closed them like scissors."

        "Whew. I felt bad for the kid at the end, who had to do like fifteen names and gestures."
        drama_teacher "Great! Now get into pairs for this next game!"
        "Nina turned to me."
        nina "Hey, want to be partners?"
        you "Okay."
        drama_teacher "With your partner, create a quick scene. BUT-- you can only use the words 'yes', 'no', 'please' and 'banana'! Start now!"
        nina "Okay, this will be great. Let's say we are secret agents. And the code word is 'banana'."
        nina "So I'm going around asking everyone 'banana' but I keep getting the wrong person! Finally you say 'banana' back and I'm just so happy! Let's try it, okay?"
        "Wow. She already had an idea? She seemed so excited... I figured I could try it."
        you "Okay."
        "She looked around exaggeratedly, and then tiptoed over to stage whisper into my ear,"
        nina "Banana?"
        "I shrugged."
        nina "(Now, stand over here so it looks like you're someone else!)"
        nina "Banana?"
        "I couldn't let her do all the acting, so I used my best tough guy voice to say,"
        you "No!"
        nina "(That's great! Okay, one more and then it'll be the right person.)"
        nina "Banana?"
        "I used a funny accent to say,"
        you "No."
        nina "(Yes! Awesome!)"
        nina "Banana!"
        "I looked around sneakily and muttered back,"
        you "Banana."
        nina "Great job! Let's practice one more time because I think we have time. I love all the different voices you did! Make sure you act like the voices, too, with your body language."
        "Wow, she was good at this. She'd clearly had some acting experience before."

        drama_teacher "Time's up! Let's see what you came up with!"
        "All the skits were silly, but we really made everyone laugh with our exaggerated motions and accents."
        drama_teacher "So many great ideas! In this club we'll be playing drama games, but we'll also be putting on a play for your parents and friends."
        drama_teacher "So I hope you will take drama club seriously, especially once parts are handed out! That's it for today!"

        "The students got up to leave and Nina turned to me."

        nina "A play! I'm so excited! I hope it's something with lots of action and drama! I wonder if it will be a musical?!"
        "She started singing,"
        nina "🎶 Some-where, o-ver the rain-bow! 🎶"

        menu:
            "What should I say?"
            "🎶 Way upppp high 🎶":
                you "🎶 Way upppp high 🎶"
                "She grins with delight and you sing the rest of the stanza together."
                $ nina_pts += 1
                nina "I can tell this year is going to be great!"
            "Is that from a musical?":
                you "Is that from a musical or something?"
                nina "Have you never seen 'The Wizard of Oz'?! You've got to watch it! You should come over and watch it with me sometime! There's lions, and tigers, and bears, OH MY!"
            "(Say nothing)":
                "It was time to go. I put on my backpack and headed to the door."
        nina "Oh no! What am I doing?! I was supposed to leave thirty minutes ago to be on time for... for something important! See you all later!"
        "She snatched up her backpack and sprinted out of the room, her curls bouncing up and down as she ran."
        "She sure had a lot of energy!"
    return

label nina2:

    return

label nina3:
    return
