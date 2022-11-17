# Afternoon Class Events
# Afternoon classes include language arts (Nina), science (Tabitha), and technology/art?
label get_event_afternoon(curr_day):
    scene classroom
    # If there's a number for today (or sequence?), do that. Otherwise, 
    # Half the time, do a random letter. The other half of the time, no event
    "Language Arts, Science, and Technology class... my classes passed by."
    return

label afternoon_a:
    scene english
    "In English class we read this weird story about a town where it was illegal to kill cats. Then we were talking about it in our groups."
    show nina at center
    nina sad "Why would anyone want to kill cats anyway?! They're adorable {b}and{/b} useful!"
    you "Maybe the old couple was allergic. Or maybe they had pet mice."
    nina mad "No one had pet mice back then!"
    you "Maybe they did. Maybe they were the very first mice people."
    nina mad "Well, the story doesn't say anything about that!"
    return
    
label afternoon_b:
    scene technology
    "In Technology class we were practicing our typing skills by typing famous quotations."
    you "To say of what is that it is not, or of what is not that it is, is false, while to say of what is that it is, and of what is not that it is not, is true."
    you "What was Aristotle thinking when he wrote that??"
    return

label afternoon_c:
    scene science
    "I was supposed to work with Tabitha on a lab measuring mass before and after combining chemicals. She wasn't talking at all."
    show tabitha at center
    tabitha sad "..."
    menu:
        "What should I say?"
        "Ask what's wrong.":
            you "What's wrong?" # TODO: should she talk about it if your relationship is good enough?
            "She just shook her head."
            you "...It seems like something's bothering you, but you don't have to talk about it if you don't want to."
            "She nodded and went to get the chemicals for our experiment. Guess she didn't want to talk about it."
        "Just do the lab.":
            you "Can you get the chemicals?"
            "She didn't even nod, just turned and headed over to the chemical station."
    return

label afternoon_d:
    scene english
    "We read a short story about two hunters trying to kill each other on an island."
    show nina at center
    you "This sounds like it should be a video game!"
    nina "That would be cool! Do you think our teacher would let you make one for your project?"
    you "Maybe... What are you doing?"
    nina "I'm writing lyrics for a song to the tune of 'Thunder' except it will say 'Hunter'! And there's dance moves that go with it! Want to work on it with me?"
    menu:
        "What should I say?"
        "Sure!":
            you "Sure, let's do it!"
            "We were able to do most of the work in class. When it came time to present, she sang loudly and with exaggerated emotion."
            nina sad "You were laughing In the grasses, While I was scheming With field glasses, Who do you think you are?!"
        "No, I'm making a video game.":
            you "No, I think I'm going to do your video game idea!"
            nina "Okay, cool!"
            "I made a short game with different paths and ways to go. They all ended in your gruesome death... except one."
            you "I don't think our teacher's going to be able to beat this game."
            nina "You might need to give her a hint!"
        "No, I'm just going to write an essay.":
            you "No, I'm just going to write an essay. Projects sound like too much work."
            nina "Yeah, but they're so much more fun!"
            "My essay turned out boring, but I didn't care."
    return

label afternoon_2:
    scene technology
    "We started off Technology class with typing lessons. I thought that was kind of dumb since I was already kind of good at typing from playing video games and talking to people there."
    "But maybe it would be nice to be faster at typing."
    you "What am I even typing??"
    you "\"Sad lad had fad\""
    you "I feel like I'm in a bad Dr. Seuss book..."       
    "I was able to get the class record for fastest typing today!"  #TODO: Make this dependent on 'grades' or 'independent'?
    return

label afternoon_4:
    "In Language Arts class we were reading \"My Side of the Mountainn\"."
    "It's a book about a kid who runs away from home to live in the woods all by himself."
    "At least I already had a house full of food to live in... "
    show nina at center
    nina mad "This book is completely unrealistic! There's no way a kid our age could live on their own in the woods!"
    menu:
        "What should I say?"
        "You're right; it's ridiculous.":
            you "Yeah, it's pretty ridiculous. Could he really survive off watercress and deer? And in the snow?!"
            nina sad "But it would be cool if he could..."
            you "I guess books don't have to be realistic... even if it could never happen, it's fun to imagine."
        "They could live alone, but not in the woods.":
            you "I could understand if he was in the city, but not in the woods!"
            nina sad "But where would he get food in the city?"
            you "People throw away so much good food! He could probably live out of trash cans."
            nina mad "Gross!"
        "A kid could totally live alone in the woods!":
            you "What are you talking about?! A kid could totally do that! He works hard and he's really smart!"
            nina sad "Do you know how much watercress you'd need to eat to get 2000 calories per day?"
            you "He didn't just eat watercress!"

    "I wonder what she would say if she knew I was living on my own..."
    return