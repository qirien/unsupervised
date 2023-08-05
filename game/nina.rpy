# Events for the Drama Club, which leads to better friendship with Nina.

# Random generic events
label nina_random:
    "We played some improv games and practiced a song."
    $ nina_pts += 1
    return

# First visit to drama club
label nina0:
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
            "She grinned with delight and we sang the rest of the stanza together."
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

    $ nina_next += 1
    return

label nina1:
    "I headed to Drama club and was one of the first people there."
    drama_teacher "Welcome, [your_name]. How's your day?"
    you "Okay."
    drama_teacher "That answer might work for most teachers, but I want the truth! Or, if you must lie, exaggerate shamelessly!"
    you "It was better than playing catch with a wasp nest, but not as good as eating chocolates in a jello bath."
    drama_teacher "Much better! Some days are like that!"

    drama_teacher "Now that everyone's here, I'm excited to share with you the play we will be performing!"
    drama_teacher "We are going to create our own play based on 'The Monkey's Paw' - have you read it?"
    "Most of us shook our heads, but Nina squealed and clapped her hands."
    drama_teacher "It's a short story, which I want you all to read on your own, but the setup is there's an object that grants three wishes, but they come true in the most terrible ways possible."
    nina "Like, you wish for an A on a test, which you get, but because you got every question exactly right the teacher thinks you cheated and you get in trouble?"
    drama_teacher "Exactly. So what we're going to do today is break up into pairs, and each pair will think of a wish gone wrong and act it out."
    "I looked around for who could be my partner. Nina was the only other person I knew in Drama club..."
    "...but she was already paired up with another girl."
    "While I was deliberating, everyone else had found a partner and I was left standing alone like a dead tree in the desert!"
    menu:
        "What should I do?"
        "Ask to join Nina's group":
            you "Ummm, Nina, can I join your group? There's an odd number..."
            nina "Sure!"
            $ nina_pts += 1
        "Ask to join a different group":
            you "Ummm, hey, can I join your group? There's an odd number..."
            nina "You can join our group!"
        "Stand around awkwardly hoping someone notices":
            you "..."
            drama_teacher "Oh, you don't have a group? Here, Nina, let [your_name] join you for a group of three."
            nina "Okay!"

    nina "So I was thinking, people always wish for money or fame or romance or something... but we should do something different! What's a really weird yet oddly understandable wish?"
    you "Ummm... bringing someone back who's gone?"
    nina "That's just like the story! We need something different!"
    "We thought for a few minutes."
    default nina1_set = set()
    menu nina1_set:
        set nina1_set
        "What about wishing for..."
        "more wishes?":
            you "Can you wish for more wishes?"
            nina "I mean, maybe, but in the case of the Monkey's Paw that's not necessarily a good thing."
            jump nina1_set
        "being really smart?":
            you "Being really smart? Like, smart enough to think of better wishes? How could that backfire?"
            nina "Ohhh, yes, you wish to be really smart, but it ends up giving you a brain disease where your brain never stops growing and eventually it gets too big for your head and you die!"
            "Nina played the wisher and I was the doctor who gave her the bad news. The other girl was her friend who came with her and cried very convincingly."
        "infinite pizza?":
            you "Infinite pizza?"
            nina "What? No, that's too obvious. You'd suffocate under a pizza avalanche or something."
            jump nina1_set
        "an enemy to disappear?":
            you "What if you wished for your enemy to disappear?"
            "I certainly wouldn't mind if Ryan disappeared." # TODO: don't say this if you're friends with Ryan
            nina "Ooh, yeah, and then your enemy literally turns invisible! So they're even MORE annoying!"
            "Nina played the wisher and I was her invisible enemy tormenting her. The other girl in our group did a good job of being the wisher's friend who tried to get Nina to stop wishing."

    "We shared our idea with the class. Some of the ideas were silly, but there were some interesting ones, too, like the one whose first wish was for wishes to always come out good."
    "Even then, the wishes weren't always good for the wisher!"
    "Then there was the wisher who kept trying to get some food, but other people kept eating it before he could. It was so sad but so funny!"
    "This was going to be an interesting play..."

    $ nina_next += 1
    return

label nina2:
    "I hadn't seen a lot of plays, but ours wasn't at all like what I thought a play would be like."
    "We hadn't even memorized lines yet -- we were still creating them."
    "Instead of auditions, we had to come up with the character we wanted to play. Most of us would play one of the people who found the object and made wishes that came out wrong."
    drama_teacher "What do you think the object should be?"
    you "In the original it was a monkey's paw..."
    nina "That's so gross! It should be a sparkling tiara or swishy cape."
    drama_teacher "It should be something the audience can see that will work for any person to hold or wear. Why don't we look in the props closet and see if we come up with any ideas?"
    "We stood up to go when a woman I didn't know came to the door."
    nina "Mom? What are you doing here... oh no! I forgot! Sorry guys, I gotta go!"
    you "Bye, Nina!"
    $ nina_pts += 1
    "She grabbed her backpack and ran out of the room with her mom."
    "The rest of us headed to the prop room, but I was thinking about Nina. This was the second time she had run out of club early... I wonder what she had going on that made her miss drama club?"

    "As I rummaged through the props, I came across the perfect 'monkey's paw'. It was..."
    menu:
        "A sombrero":
            $ drama_lucky_object = "sombrero"
            you "Hey, what about this big hat?"
            drama_teacher "It certainly is large and easy to see!"
        "A huge ruby amulet":
            $ drama_lucky_object = "ruby amulet"
            you "Hey, what about this red amulet?"
            drama_teacher "It certainly is large and shiny!"
        "A giant pom pom keychain":
            $ drama_lucky_object = "jackalope tail"
            you "Hey, what about this pom pom thing?"
            drama_teacher "It certainly is unique!"
            you "And so soft... we could call it a rabbit's tail."
            student "Or a jackalope tail!"

    "Someone found a rain hat, and there was an old pocket watch, and a creepy-looking book. But we eventually decided on the [drama_lucky_object]."
    "Then we worked in our groups on our scenes. We acted out the wisehs, and then had to somehow get the [drama_lucky_object] to the next group."
    "I was supposed to work with Nina but she wasn't there... we muddled through it anyway, but it wasn't very good."

    $ nina_next += 1
    return

label nina3:
    "Play practice! I asked Nina why she wasn't there and she wouldn't tell me! She is bullied, giving hints about why she won't talk."

    "Nina and I both showed up to Drama club early."
    nina "If all the adults died one day, what would you do?"
    menu:
        "I would..."
        "Do the same stuff I do now":
            you "I would probably just do the same things. Go to school, hang out with friends, eat, sleep."
            "That's what I've been doing this whole time." # TODO: different response depending on stats?
        "Party!":
            you "I would party! Eat all the ice cream! Watch movies all day! No school, no work, nothing!"
            "That's what I said... and I guess when I was home by myself I kind of did that."

        "Keep everyone alive":
            you "Someone has to make sure everyone has enough food and shelter and stays alive. That would be me."
            "After all, I'd been keeping myself alive this whole time."

    "I wanted to tell her that my mom was gone... even though she wasn't dead it was almost as if she were."
    "But I couldn't tell her."
    you "Hey, where did you have to go last time? Our group was terrible without you."
    nina "Awww, did you miss me? Sorry I had to leave; sometimes I have... appointments."
    "That was vague... why didn't she want to tell me?"
    menu:
        "What should I say?"
        "What kind of appointments?":
            you "What kind of appointments?"
            nina "Just... stuff, okay!"
        "Why don't you want to tell me?":
            you "Why don't you want to tell me where you were?"
            nina "What? I'm not... it doesn't matter, okay?"
        "Okay.":
            you "Uh, okay."
            "I didn't want to be annoying about it. What if it was some embarrassing medical thing that she didn't want to talk about? She'd tell me if she wanted to."
    drama_teacher "Ahem, thespians! Let's start! I'll give each group a few minutes to practice, and then we'll all watch each other's scenes and offer honest feedback."

    student "What's a thespian?"
    nina "It's an actress, or actor! Like me, or--"
    student2 "Oh, please. Just because you were in a commercial doesn't make you an actress. Anyone could smile and wave at the camera."
    "She gave a fake smile and waved like a Barbie doll. Some kids laughed, but when I saw the hurt look on Nina's face, I didn't."
    nina "I didn't mean--"
    student2 "'And that's why you should choose Green Tree, like me!' Ugh, that commercial annoys me so much."
    drama_teacher "Okay, that's enough of that. Everyone needs to go practice their scenes, now!"

    "Everyone moved off to their groups, leaving the three of us to practice. Nina took a deep breath, closed her eyes, and when she opened them, she smiled."
    nina "O-okay. Let's start!"
    menu:
        "What should I say?"
        "She was mean.":
            $ nina_pts += 1
            you "That was mean, how she was making fun of you."
            nina "Maybe. I mean, she's kinda right, though. That commercial is terrible. Every time it comes on I just have to look away so I don't see that stupid fake smile on my face."
            you "I never even knew you were in a commercial. That's kinda cool."
            nina "It's not a big deal."
        "Yeah, let's move on.":
            you "Okay, Nina."
        "Are you okay?":
            you "Are you okay? You seem kinda upset."
            nina "I'm fine! I mean, she's right about that commercial. It's terrible, and literally the worst performance of my life."
            you "I never even knew you were in a commercial. That's kinda cool."
            nina "It's not a big deal."
            $ nina_pts += 1

    "We practiced our scene. It went much better with Nina there. And she seemed to feel better after a few minutes."

    # TODO: finish this? perform them and mean girls give mean feedback?

    $ nina_next += 1
    return

label nina4:
    "Nina apologizes and explains what's going on. She has to decide whether to be in the school play or take an acting job"
    $ nina_next += 1
    return

label nina5:
    "The school play! Either Nina performs or she watches the play. You forget a line but it's ok!"
    $ nina_next += 1
    return

label nina6:
    "Great job on the school play everyone! Nina appreciates your support!"
    $ nina_next += 1
    return

label nina_final:
    "We don't have a play, so we're just helping the teacher out. Nina isn't there, though."
    return
