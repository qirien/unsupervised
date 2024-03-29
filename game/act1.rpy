label act1:
    scene bedroom day
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
    "We've ridden past Bradbury Middle School lots of times on our way to the grocery store, so I knew how to get there. It took me a few minutes to figure out where to park my bike, though."

    "I took out my schedule and looked over it again. First was advisory in 103... I think it's kind of like homeroom?"

    "My mom had printed out a map for me. It reminded me of the maps we used on our adventures in the woods or around town."
    "Sometimes she'd hand me the map and make me give her directions. Even if I said to go the wrong way, she'd turn the car wherever I said to go... at least, until I started just always giving directions to the ice cream shop."

    "Anyway. Where's room 103?"
    call find_class("103")

    scene school hallway
    "I headed off towards 103. I knew I was going the right way when I passed the library, just like the map said."
    "Hey, isn't that Ryan from elementary school?! She's so much taller now! We used to eat lunch together all the time."
    you "Hey, Ryan!"
    "She stopped, looked right at me, and then scowled and started to walk away."
    you "Wait, Ryan! Don't you recognize me?"
    ryan "Yeah, but don't act like we're friends."
    "Ryan's Friend" "Who is that?"
    ryan "Oh, just someone I know. Nobody important."
    
    menu:
        "I felt..."
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

    "I was still upset by the time I reached room 103."           

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
    math_teacher "Welcome to Bradbury Middle School! In Advisory we'll hear announcements, take care of problems, and mostly just hang out together once a week."
    math_teacher "You can do homework in here or chat if we don't have anything else going on. But we won't have time for that today! We're going to play a game!"
    "He had so much energy... I couldn't decide whether to groan or smile."
    math_teacher "First, I need everyone to fill out this form. There's just three questions, and one of them is your name, so I know all of you can do it."
    "I got a paper. My pencil felt foreign in my hands... would I even remember how to write? All summer I'd been biking, traveling, or playing video games."

    call screen info_sheet()
    math_teacher "Time's up! Now, I want you to take the beautiful paper you worked so hard on... and crumple it up into a ball."
    "I waited a moment for the punchline, but it turned out he was serious, so I crumpled my paper."
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
    ryan "Umm... [she_he] like[she_he_s] to [hobby] and [her_his] favorite food is [favorite_food]. [she_he!c] hate[she_he_s] it when teachers [hated_action]. That's it."
    "I pushed away the memory of the time I brought [favorite_food] to school and shared it with Ryan as we laughed about something silly... That wasn't who she was anymore."

    "Soon it was my turn to read."
    you "This paper is by Emir...?"
    show emir happy at quarterright
    emir sad "That's me! Don't make me sound stupid, ok?"
    ryan "You already sound stupid."
    math_teacher "Hey, in this class, I expect everyone to talk respectfully to and about each other."
    "He looked at Ryan, but she just rolled her eyes and I continued."
    you "Emir hates it when teachers are boring, and he likes tacos and playing flag..."
    "I could barely read the next word. It looked like 'fartball' but it was probably supposed to be 'football'..."
    menu:
        "What should I say?"
        "Fartball":
            you "...fartball."
            show emir happy with dissolve
            "The class exploded with laughter. Emir just looked at me for a second, and I grinned at him. Finally, he laughed and shook his head."
            emir "Yeah, I'm pretty good at fartball, but not as good as you, I bet!"
            $ emir_pts += 2
        "Football":
            you "...football."
            show emir happy with dissolve
            "Emir looked at me and nodded."
            $ emir_pts += 1
        "I'm sorry, I can't read this.":
            you "Sorry, his handwriting's too messy, I can't read this."
            $ emir_pts -= 1
            emir angry "It says football! Obviously! What else comes after 'flag'?!"
            you "Oh, okay, flag football."
    hide emir with dissolve
    "By the time the rest of the class introduced themselves, advisory was over."
    math_teacher "One more thing -- tomorrow at lunch all the clubs and sports will have booths. Go check them out! It's a great way to make new friends and do cool stuff!"
    "Clubs? Sports? In elementary school we had after school clubs, but sometimes they felt more like babysitting. Maybe middle school would be different."
    "After advisory, I had gym, math, and social studies. By the time it was lunch I was really hungry!"

    menu:
        "Should I use my map or follow the crowd?"
        "Use my map":
            call find_class("the cafeteria")
        "Follow the crowd":
            "Everyone seemed to be headed the same way, so I just went that way too. Sure enough, we ended up at the cafeteria."

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
                    "That was really weird. I couldn't really understand why someone would make a big mess like that."
                "Scary.":
                    $ anxious += 1
                    "If they would do that to a milk carton, what would they do to someone that annoyed them? I stayed far away from them."
                "Cool.":
                    $ rebellious += 1                    
                    "Cool. It was like a homemade water gun."
        "Sit by someone who's sitting alone.":
            show tabitha angry at center with dissolve
            "I sat by a girl wearing baggy pants and a sticker on her water bottle from a hiking area I'd been to."
            you "You like to go hiking?"
            "She glared at me, like I'd interrupted something important."
            you "Uh, your sticker. I went hiking there once."
            tabitha sad "...It's okay."
            "We ate quietly for a few minutes."
            menu:
                "What should I say?"
                "Talk about the food":
                    you "This chicken sandwich isn't too bad."
                    "She shrugged."
                "Talk about school":
                    you "What did you guys do in advisory this morning?"
                    tabitha "Just talked."
                "Don't talk about anything":
                    "I continued to eat quietly, and so did she."
            "She finished eating and pulled out a book. It looked like an old book from the cover, though I couldn't see the name."
            
            "Seems like she wants to be left alone."
    
    scene school
    "After lunch and a few more classes, I rode my bike home."
    scene house evening
    "Even though the house was empty, it still felt cozy, like a warm hoodie."
    scene bedroom day
    "I had some time to do a few things before dinner..."
    call freetime_menu(2)
    
    "...Mom still wasn't home. Guess I was making my own dinner."
    "We had some basic ingredients in the fridge, and I'd cooked for the two of us plenty of times before."
    call meal_menu

    scene bedroom night

    "Wow, my mom was really working late. That's not too unusual, but I was all by myself in our quiet house."
    menu:
        "I felt..."
        "empowered":
            "Nothing against my mom, but I liked being in charge of my own time and meals and stuff."
            "I texted her and told her that I was home from school and doing fine."
            $ independent += 1
        "worried":
            "I started to worry about her. What if she'd been a car accident on the way home from work? Or what if she had a heart attack or something? Sometimes those things happened!"
            $ anxious += 1
            "I texted her and asked where she was, but she didn't respond right away. Sometimes she couldn't check her phone at work."
        "devious":
            "If my mom wasn't here, I could do anything I wanted."
            scene master bedroom evening            
            "I went up to her room and looked through her stuff. I found some jewelry and tried it on. Not bad, not bad."
            "I put everything away afterwards. She'd never know."
            $ rebellious += 1
            "I texted her a photo of me making a funny face."
        
    # TODO: show phone interface here?
    "My phone was a locked down phone and couldn't install apps, so I mostly used it to take pictures and talk to my mom."
    "My dad texted me once in a while; random stuff like a photo of his lunch or from some trip he was on."
    
    scene bedroom night
    "Mom had never worked this late before... but I couldn't stay up forever. I sent her a good night text and went to bed."
    return

# DAY 2
label wakeup2:
    
    scene bedroom day
    "I woke up the next day to my alarm and the feeling that something was wrong."
    "Everything looked the same as last night..."
    "...Where was Mom?"
    scene master bedroom day
    "Her bed hadn't been slept in."
    scene kitchen 
    "No food was missing from the fridge."
    scene house hallway    
    "There was no new note on the table; no new texts on my phone."    
    scene kitchen    
    "I searched the house, calling for her and checking every room."
    you "Mom??"
    "What if something had happened to my mom at work? They would have no way to contact me - only my parents had my number."

    # TODO: sfx
    "A song suddenly started playing, and my heartbeat raced like a startled deer."
    "It was my mom's phone."
    scene house hallway
    "I searched around and found it on the floor but still plugged in."
    "She must have plugged it in to charge and it fell down and she forgot it."
    "She was supposed to be a brilliant scientist, but she was always forgetting things like that."

    menu:
        "What should I do?"
        "Try to unlock it":
            "People were always telling my mom and I that we looked alike, so I could sometimes fool the face ID."
            "I never told my mom that, though..."
            "I picked it up and looked at it... and it unlocked."
        "Leave it alone":
            "I picked it up to put it away... wow, lots of notifications."
            "...I only looked at it for a minute when it unlocked."
            "People were always telling my mom and I that we looked alike, so I could sometimes fool the face ID."
            "Guess as long as her phone's unlocked I should make sure she's not in trouble or anything..."
    
    # TODO: have a phone interface where you can choose order to check Calendar, Messages, and ...?
    "There was my text from last night, and also some texts from people I didn't recognize."
    "The calendar from yesterday had an event on it called 'Field Test'."
    "Maybe she was still at the field test? And she couldn't call me because she left her phone here?"
    "But wouldn't she have borrowed someone else's?"
    "Should I call the police? Or my dad? Or one of her coworkers?"
    "I needed to know more first. I started to read her messages."
    # TODO: phone interface, allow to read texts such as
    nvl clear
    coworker_text "Where did you go?! You weren't at the drop site. I'm guessing you have no reception since we haven't heard from you."
    coworker_text "Anyway, we found the bug; it was a bit shift error in the interface between the input hardware and the main system."
    coworker_text "I told Jen we needed tests for everything, but she thought the deadline was more important. Anyway, call us when you can!"
    "Drop site? Bit shift error? This looked like work stuff."
    you "I guess something went wrong and my mom wasn't where they thought she would be. He didn't sound too worried, though..."
    default act1_contact_set = set()
    menu act1_contact:
        set act1_contact_set
        "What should I do?"
        "Text the coworker":
            you_text "This is her kid... Where is my mom? Why didn't she come home?"
            coworker_text "Oh, [your_name], right? I'm really sorry... I, uh, I'm not really supposed to talk about the project..."
            coworker_text "But I'm reasonably sure that your mom is safe! We just don't really know where she is..."
            coworker_text "Are you okay? Do you have someone taking care of you? Do you need me to, I don't know, call someone or something?"
            you_text "I'm taken care of. I'm kinda worried though..."
            "I mean, it wasn't technically lying. I did have someone taking care of me -- myself."
            coworker_text "Don't worry! We'll figure this out. And I'll let you know if I talk to your mom, okay?"
            you_text "Okay."
            $ met_mark = True
            jump act1_contact
        "Call the police":
            "I started to dial the emergency number... but then stopped. What would happen if I did? Would they take me away to live with some strangers? Would they think my mom wasn't doing a good job and send me to live with my dad?"
            "I didn't want either of those things to happen."            
            jump act1_contact
        "Call dad":
            "Dad wasn't around much, but parents are supposed to be there for their kids, right?"
            "I called his number from my mom's phone, but no one answered. I called him from my phone, and he still didnt' answer."
            "I called him four more times, and he never picked up."
            "No, he wasn't going to be any help. And even if he did answer and invited me to stay with him, would I want to do that?"
            "I remembered the last time I was there...We did go to the amusement park together... but then he wandered off. I spent the day going on rides all by myself."
            "He showed up at the end of the day and took me home without even apologizing."
            "He spent the rest of my visit doing stuff on his computer. Whenever I'd ask him about it, he'd tell me to go away because I was making him lose his concentration."
            "No, I didn't need his help."
            jump act1_contact
        "Nothing":
            $ pass
        
    "It looked like I was on my own, for now. I'd figure this out later; for now, I had to get to school."
    "If I was late or absent, the school might try to contact my parents."
    "And when they couldn't contact them, they might decide I needed to live somewhere else, with total strangers telling me what to do."    
    "I hopped on my bike and headed off to school."
    return

return
