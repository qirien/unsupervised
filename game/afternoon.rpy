# Afternoon Class Events
# Afternoon classes include language arts (Nina), science (Tabitha), and technology/art?
label get_event_afternoon(curr_day):
    scene classroom
    "Language Arts, Science, and Technology class... my classes passed by."
    return

label afternoon_a:
    "In English class we read this weird story about a town where it was illegal to kill cats. Then we were talking about it in our groups."
    show nina at center
    nina sad "Why would anyone want to kill cats anyway?! They're adorable {b}and{/b} useful!"
    you "Maybe the old couple was allergic. Or maybe they had pet mice."
    nina mad "No one had pet mice back then!"
    you "Maybe they did. Maybe they were the very first mice people."
    nina mad "Well, the story doesn't say anything about that!"
    return
    
label afternoon_b:
    ""
    return

label afternoon2:
    "We started off Technology class with typing lessons. I thought that was kind of dumb since I was already kind of good at typing from playing video games and talking to people there."
    "But maybe it would be nice to be faster at typing."
    "I was able to get the class record for fastest typing today!"
    return

label afternoon4:
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
            nina sad "Do you know how much watercress you'd need to eat to get 2000 calories per day? "
    return