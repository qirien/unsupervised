label act1:
    scene bedroom
    "It's morning, but nobody's going to wake me up for school."
    "I'm in sixth grade and I'm doing everything on my own."
    "No mom, no dad, no rules but mine."
    menu:
        "Living on my own is..."
        "...exactly what I want to do.":
            "I love the feeling of being in charge of everything I do! Sure, I miss my mom, but I love this freedom."
            $ independent += 1
        "...lonely and sad.":
            "I miss my mom. I wish I didn't have to do this all by myself."
            $ anxious += 1
        "...too much work.":
            "I like doing my own thing, but I don't like having to do all the work. Sometimes I miss my mom."
            $ rebellious += 1

    "I didn't always live like this. It started a few weeks ago on the first day of school."

    # DAY 1
    scene kitchen
    "Yeah, that's right -- my mom wasn't even there for my first day of middle school."
    "I'm used to doing things on my own - I biked home from school last year, and when my mom works late sometimes I make dinner."
    "But on the first day of school I woke up to this note on the table."
    note "Had to leave early for a big work thing. I might be home late. Good luck today; you'll do great! Don't forget to brush your teeth! - Mom"

    "I got myself some food and hopped on my bike to head to school."
    scene house day
    "Unlike my mom, at least my bike was always there for me."
    "It was a birthday present from my dad... but he just ordered it online and it arrived in pieces in a big box. No card, not even a note."
    "My mom was the one who put it together with me."

    scene school
    "We've ridden past the middle school lots of times on our way to the grocery store, so I knew how to get there. It took me a few minutes to figure out where to park my bike, though."

    "I took out my schedule and looked over it again. First was advisory in 105... I think it's kind of like homeroom?"

    "My mom had printed out a map for me. It reminded me of the maps we used on our adventures in the woods or around town."
    "Sometimes she'd hand me the map and make me give her directions. Even if I said to go the wrong way, she'd turn the car wherever I said to go... at least, until I started just always giving directions to the ice cream shop."

    "Anyway. Where's room 105?"
    #scene school-map

    scene school hallway
    "I headed off towards 105. I knew I was going the right way when I passed the library, just like the map said."
    "Hey, isn't that Ryan from elementary school?! She's so much taller now! We used to eat lunch together all the time."
    you "Hey, Ryan!"
    "She stopped, looked right at me, and then scowled and started to walk away."
    you "Wait, Ryan! Don't you recognize me?"
    ryan "Yeah, but don't act like we're friends."
    "Ryan's Friend" "Who is that?"
    ryan "Oh, just someone I know. Nobody important."
    
    menu:
        "How did that make me feel?"
        "Furious":
            $ independent += 1
            "That made me so mad! We ate lunch together every day, and she always wanted to play tetherball, and I played it with her even though I don't even like tetherball!"
            "But I wasn't going to let her make me late for class. I stalked onwards."
        "Embarassed":
            $ anxious += 1
            "My cheeks started to feel hot. Was everyone looking at me, thinking I was 'nobody important'?"
            "I had to get out of there."
        "Bitter":
            $ rebellious += 1
            you "Oh, sorry, I thought you were someone else. Someone who knows what the word 'friend' means."
            "She rolled her eyes at me and walked off."

    "I was still upset by the time I reached room 105."           

    scene classroom
    "It looked like a math classroom, with origami cubes and stars hanging from the ceiling and posters about lines and angles and equations."
    "I stood in the back for a second, trying to decide where to sit. I didn't see any of my friends from 5th grade."
    menu:
        "Where should I sit?"
        "Near the front, so I could ask questions easier.":
            $ independent += 1
            "I sat down and got out my notebook and pencil, ready to take notes."
        "In the middle, so no one would notice me.":
            $ anxious += 1
            "I sat down and looked around. It felt weird not to have anyone to talk to... I got out my notebook and pencil so I would have something to focus on."
        "In the back, so the teacher couldn't watch me as well.":
            $ rebellious += 1 
            "I sat down and got out my pencil so I'd have something to do with my hands. I started drumming it lightly on the table to a steady beat."
    "Ryan walked in just as the bell rang, and the teacher began."
    math_teacher "Welcome to middle school! In Advisory we'll hear announcements, take care of problems, and mostly just hang out together once a week."
    math_teacher "You can do homework in here or chat if we don't have anything else going on. But we won't have time for that today! We're going to play a game!"
    "He had so much energy... I couldn't decide whether to groan or smile."
    math_teacher "First, I need everyone to fill out this form. There's just three questions, and one of them is your name, so I know all of you can do it."
    "I got a paper. My pencil felt foreign in my hands... would I even remember how to write? All summer I'd been biking, traveling, or playing video games."

    #screen info_sheet
    math_teacher "Time's up! Now, I want you to take the beautiful paper you worked so hard on... and crumple it up into a ball."
    "I waited a moment for the punchline, but I guess he was serious, so I crumpled my paper."
    math_teacher "Now we'll have a snowball fight until I blow the whistle!"
    "He threw his paper at me, and I ducked. I threw mine back at him, and soon everyone was throwing paper balls at each other."
    show emir happy at center with dissolve
    "One smacked me in the side of the head. I turned to see a kid smirking at me and then look away."
    "I waited until he wasn't looking, and then aimed it right at the back of his head. At that moment, he turned, and it caught him right on the nose."
    "Kid" "Oww! Ha ha ha!"
    hide emir with dissolve
    show math_teacher with dissolve
    "The whistle blew, and the last few balls of paper flew through the air. Our teacher caught the last one in mid-air."
    math_teacher "And...stop! Now, everyone take one ball of paper that's near you. Make sure it's not yours. We'll go around the classroom, and you tell us about the person whose paper you have."

    "The stream of names washed over me like a summer thuderstorm. There was no way I was remembering all of these people."
    ryan "Okay, my paper is by... [your_name]."
    "She paused and scowled."
    ryan "Umm... [she_he] likes to [hobby] and [her_his] favorite food is [favorite_food]. [she_he] hates it when teachers [hated_action]. That's it."
    "I pushed away the memory of the time I brought [favorite_food] to school and shared it with Ryan as we laughed about something silly... That wasn't who she was anymore."

    "Soon it was my turn to read."
    you "This paper is by Emir...?"
    emir sad "That's me! Don't make me sound stupid, ok?"
    ryan "You already sound stupid."
    math_teacher "Hey, in this class, I expect everyone to talk respectfully to and about each other."
    "He looked at Ryan, but she just rolled her eyes and I continued."
    you "Emir hates in when teachers are boring, and he likes tacos and playing flag..."
    "I could barely read the next word. It looked like 'fartball' but it was probably supposed to be 'football'..."
    menu:
        "What should I say?"
        "Fartball":
            you "...fartball."
            "The class exploded with laughter. Emir just looked at me for a second, and I grinned at him. Finally, he laughed and shook his head."
            emir "Yeah, I'm pretty good at fartball, but not as good as you, I bet!"
            $ emir_pts += 2
        "Football":
            you "...football."
            "Emir looked at me and nodded."
            $ emir_pts += 1
        "I'm sorry, I can't read this.":
            you "Sorry, his handwriting's too messy, I can't read this."
            $ emir_pts -= 1
            emir "It says football! Obviously! What else comes after 'flag'?!"
            you "Oh, okay, flag football."
    "By the time the rest of the class introduced themselves, advisory was over."
    math_teacher "One more thing -- tomorrow at lunch all the clubs and sports will have booths. Go check them out! It's a great way to make new friends and do cool stuff!"
    "Clubs? Sports? In elementary school we had after school clubs, but sometimes they felt more like babysitting. Maybe middle school would be different."

    scene black
    # TODO: more map class-finding minigame?
    "After a few classes, and only getting lost twice, I made it to lunch."
    scene cafeteria
    "I waited in line for a chicken sandwich with tater tots and orange slices. Then I had to try and figure out where to sit..."
    "I didn't see anyone I knew. Well, Ryan was in the corner with her new friends, but I wasn't going to sit by her!"
    menu:
        "Where should I go?"
        "Sit by yourself.":
            "I just sat by myself and ate my lunch. Some kids started throwing the tater tots back and forth, but a teacher stopped that pretty fast."
            "After I finished my lunch, I went outside and walked around. There were some kids throwing a ball against the wall, and some walking around the track."
            "One took their milk carton and jumped on it, spraying chocolate milk all over the sidewalk."
            menu: 
                "Wow. Middle school kids were..."
                "Weird.":
                    $ independent += 1
                "Scary.":
                    $ anxious += 1
                "Cool.":
                    $ rebellious += 1
        "Sit by someone who's sitting alone.":
            "I sat by a girl wearing baggy pants and a t-shirt from a hiking area I'd been to."
            you "You like to go hiking?"
            tabitha "What?"
            you "Your shirt. I went hiking there once."
            tabitha "It's okay. We go a lot."
            you "You and your family?"
            tabitha "Me and my dad, yes."
            "We ate quietly for a few minutes."
            menu:
                "What should I say?"
                "Talk about the food":
                    you "This chicken sandwich isn't too bad."
                "Talk about school":
                    you "What did you guys do in advisory this morning?"
                "Don't talk about anything":
                    "I continued to eat quietly, and so did she."
            
    
    
    
    
    
    
    
    
    # DAY 2
    
    
    
    # scene cafeteria
    "As I waited in line for my lunch, I noticed that all the clubs and teams had setup booths around the cafeteria to try to get people to join."
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
    emir "Oh, I had a class in the Makerspace this morning. It's like a room with tools and materials and you can make things. Sometimes they have robots and 3D printers and stuff. So Maker's Club is making things there."
    "We got our food and Emir sat down at an empty table. I looked around, but I didn't see anyone else I knew."

return