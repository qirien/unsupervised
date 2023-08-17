# Morning Class Events
# Morning classes include advisory (Emir), gym, math (Calvin), social studies
label morning_default:
    scene classroom
    "Advisory, gym, math, social studies... I went to class like a good little robot."
    return

label morning_a:
    "In gym class we played ultimate frisbee. I felt like I ran up and down the field a hundred times!"
    "The frisbee is coming my way!"
    $catch = renpy.random.randint(0,3) # TODO: have this based on whether you do physical activities or not
    if (catch == 2):
        "I caught it, and passed it on to my teammate to score!"
        "I made sure I was open to catching more passes and helped my team score points."
    else:
        "I tried to catch it, but it just bounced off my hand."
        "No one passed to me again after that, so I just played defense."
    return

label morning_b:
    "In Social Studies class we were learning about ancient Egypt."
    "Even back then kids had to go to school, but they also learned skills and played games."
    "Our teacher had us write a short story about a kid living in ancient Egypt."
    "I decided to write about..."
    menu:
        "A rich kid who lived in the palace":
            you "Akila knew how to read and write and she loved playing Dogs and Jackals with her dad..."
        "A slave kid who worked hard on a farm":
            you "The only time Asim got to play was when the floods came. But this time, they said he was old enough to help build a great statue..."
        "An orphan kid who lived on his own":
            you "Omari ran away from being a slave and snuck into the palace school. The tutor was so impressed with his bravery that he invited him to come learn every day..."
    "Kids often died from diseases and accidents... it was hard to imagine living in such a dangerous time."
    return

label morning_c:
    "Sometimes, math was all lectures and worksheets..."
    "...but sometimes we had to work in groups."
    show calvin at center
    calvin "Don't expect me to do all the work in our group just because I'm good at math."
    menu:
        "What should I do?"
        "Work as little as possible.":
            $ rebellious += 1
            you "You can't expect me to do all the work, either! I don't even know what to do."
            calvin mad "It's so easy! Look, you just do it like this..."
            "I was able to get Calvin to do most of the work by pretending I didn't know how."
        "Make a plan for splitting things up evenly.":
            $ independent += 1
            you "Obviously. You answer the evens, I'll do the odds, then we'll check each other's work."
            calvin "That... that sounds fair."
        "Just work by yourself so you don't have to deal with other people.": 
            $ anxious += 1
            you "Let's just work on our own."
            calvin "Fine, I don't trust your answers anyway."
    return

# Day 14 morning event
# TODO: adjust timing as needed
label morning_14:
    scene classroom
    math_teacher "Today in advisory we're taking a career test."
    math_teacher "This important test will determine your entire future..."
    "The class was silent. He had our attention."
    math_teacher "...of 6th grade career test results. That's all."
    math_teacher "In other words, it's not that big a deal! It's just for fun and to give you some ideas."
    "He gave us the website address and we started taking the quiz."
    quiz "Choose your three favorites."
    # R ealistic, practical, doers
    # I deas, intellectual
    # A rtistic, expressive
    # S ocial, helpers, teachers
    # E nterprising, working with people and data
    # C onventional, working with data and rules
    # from Holland Codes, a taxonomy of interests, https://en.wikipedia.org/wiki/Holland_Codes
    $ career_pts = {"R":0, "I":0, "A":0, "S":0, "E":0, "C":0}
    $ career_names = [
    ("Accountant", "IEC"),
    ("Actuary", "IEC"),
    ("Advertiser", "IAE"),
    ("Architect", "RAE"),
    ("Artist", "A"), 
    ("Athlete", "R"),
    ("Buyer", "C"),
    ("Carpenter", "RIC"), 
    ("Chef", "RAE"), 
    ("Chemist", "RIC"), 
    ("Community Health Worker", "ISE"),
    ("Computer Programmer", "RIC"),
    ("Counselor", "IAS"),
    ("Customer Service Representative", "SEC"),
    ("Dentist", "RIS"), 
    ("Diplomat", "ASE"),
    ("Doctor", "RIS"),
    ("Driver", "R"),
    ("Economist", "ISC"),
    ("Educational Administrator", "SEC"),
    ("Engineer", "RIC"),
    ("Entrepreneur", "ASE"),
    ("Farmer", "R"), 
    ("Fashion Designer", "RAE"),
    ("Financial Analyst", "IEC"),
    ("Financial Planner", "SEC"),
    ("Firefighter", "RSE"),
    ("Fundraiser", "E"),
    ("Graphic Designer", "RAE"), 
    ("Human Resources Worker", "SEC"),
    ("Lawyer", "ISE"),
    ("Librarian", "ISC"),
    ("Market Research Analyst", "ISE"),
    ("Musician", "RAE"), 
    ("Nurse", "RSC"), 
    ("Nutritionist", "ISE"),
    ("Paralegal", "IEC"),
    ("Park Naturalist", "RAS"), 
    ("Personal Trainer", "RSE"),
    ("Pharmacist", "ISC"),
    ("Photographer", "RAE"),
    ("Physical Therapist", "RIS"),
    ("Physicist", "I"),
    ("Professor", "I"),
    ("Property Manager", "E"),
    ("Psychologist", "IAS"),
    ("Religious Leader", "ASE"),
    ("Salesperson", "SEC"),
    ("Sports/Wilderness Physician", "RIS"),
    ("Surgeon", "RIS"),
    ("Teacher", "S"),
    ("Translator", "RAS"),
    ("Tutor", "ISE"),
    ("Veterinarian", "RIS"),
    ("Wildlife Biologist", "RIC"),
    ("Writer", "A")
    ]
    
    default morning_14_set1 = set()
    default morning_14_set2 = set()
    default morning_14_set3 = set()
    default morning_14_set4 = set()  
    $ add_amount = 3  
    label morning_14_career1:
        if (len(morning_14_set1) >= 3):
            $ add_amount = 3
            jump morning_14_career2
        menu:        
            set morning_14_set1
            "I would rather be..."
            "Making something useful":
                $ career_pts["R"] += add_amount
            "Thinking about how to make something":
                $ career_pts["I"] += add_amount
            "Making something look beautiful":
                $ career_pts["A"] += add_amount
            "Making something that helps someone":
                $ career_pts["S"] += add_amount
            "Leading a group to make something":
                $ career_pts["E"] += add_amount
            "Following instructions to make something":
                $ career_pts["C"] += add_amount
        $ add_amount -= 1
        jump morning_14_career1

    label morning_14_career2:
        if (len(morning_14_set2) >= 3):
            $ add_amount = 3
            jump morning_14_career3
        menu:
            set morning_14_set2
            "In a zombie apocalypse, I would probably be..."        
            "In the middle of the action.":
                $ career_pts["R"] += add_amount
            "Studying the best survival techniques.":
                $ career_pts["I"] += add_amount
            "Keeping up morale.":
                $ career_pts["A"] += add_amount
            "Running a school or clinic.":
                $ career_pts["S"] += add_amount
            "The leader helping everyone see the big picture":
                $ career_pts["E"] += add_amount
            "Keeping everything organized.":
                $ career_pts["C"] += add_amount
        $ add_amount -= 1
        jump morning_14_career2

    label morning_14_career3:
        if (len(morning_14_set3) >= 3):
            $ add_amount = 3
            jump morning_14_career4
        menu:
            set morning_14_set3
            "If I worked at a school, I would be..."        
            "A PE/computer/shop teacher":
                $ career_pts["R"] += add_amount
            "A science teacher":
                $ career_pts["I"] += add_amount
            "An art/music/drama teacher":
                $ career_pts["A"] += add_amount
            "The school nurse/counselor":
                $ career_pts["S"] += add_amount
            "The principal":
                $ career_pts["E"] += add_amount
            "A librarian or math teacher":
                $ career_pts["C"] += add_amount
        $ add_amount -= 1
        jump morning_14_career3
    
    label morning_14_career4:
        if (len(morning_14_set4) >= 3):
            jump morning_14_career5
        menu:
            set morning_14_set4
            "If I have to do chores I dislike, I'm most likely to..."
            "Just jump in and start working.":
                $ career_pts["R"] += add_amount
            "Study cleaning chemicals and choose the best method.":
                $ career_pts["I"] += add_amount
            "Put on some good music or sing while I work.":
                $ career_pts["A"] += add_amount
            "Think about how much I'm helping my family while I work.":
                $ career_pts["S"] += add_amount
            "Persuade a friend to help me.":
                $ career_pts["E"] += add_amount
            "Make a list first and enjoy checking off each item.":
                $ career_pts["C"] += add_amount
        $ add_amount -= 1
        jump morning_14_career4
    
    label morning_14_career5:
        "Okayyyyy, that was kind of a weird test."
        nvl clear

        # Pop off the three smallest ones and we're left with the three most chosen options.
        $ career_pts.pop(min(career_pts, key=career_pts.get))
        $ career_pts.pop(min(career_pts, key=career_pts.get))
        $ career_pts.pop(min(career_pts, key=career_pts.get))
        $ career_acro = ""
        $ career_most = max(career_pts, key=career_pts.get)

        $ career_desc = "You like:\n"
        if "R" in career_pts:
            $ career_desc += "things that are practical and realistic\n"
            $ career_acro += "R"
        if "I" in career_pts:
            $ career_desc += "thinking about ideas and understanding concepts\n"
            $ career_acro += "I"
        if "A" in career_pts:
            $ career_desc += "being creative and artistic\n"
            $ career_acro += "A"
        if "S" in career_pts:
            $ career_desc += "helping or teaching people\n"
            $ career_acro += "S"
        if "E" in career_pts:
            $ career_desc += "leading and persuading people\n"
            $ career_acro += "E"
        if "C" in career_pts:
            $ career_desc += "structure, order, and organization\n"
            $ career_acro += "C"
        $ career_desc = career_desc.rstrip()
        quiz "[career_desc]\n"
        $ career_desc = "You should think about careers such as:\n"

        $ i = 0
        $ career_name = "Student"
        while (i<len(career_names)):
            $ career_pair = career_names[i]
            if ((career_pair[1] == career_acro) or (career_pair[1] == career_most)):
                $ career_desc += career_pair[0] + "\n"
                $ career_name = career_pair[0]
            $ i+= 1
        quiz "[career_desc]"
        # TODO: improve formatting of quiz character so this can fit all the options and look nice

        show emir happy at center
        emir "This says I should be a chef! What does yours say?"
        you "It says I should be a [career_name]..."
        emir "Ha! I can't picture you as a [career_name]."
        menu:
            "What should I say?"
            "I could be a [career_name]!":
                you "I could totally be a [career_name] if I wanted to!"
                emir "Yeah, but why would you want to?"
                you "Who knows why adults pick their jobs? I mean, does anyone grow up thinking, 'I want to be a market research analyst!'"            
                emir "As a little kid you only know about the cool jobs that you see in cartoons."
                you "I still only know about the cool jobs you see in cartoons. I don't even know what some of these jobs are."
                emir "They should let us test them out! Like you test drive a car!"
                you "Oh sure, they'll just let you be the nuclear power plant operator for a day. We'll see how that goes!"
                emir "They could make sure you don't do anything terrible..."
            "There's no way you're becoming a chef.":
                you "It's more likely than you becoming a chef. Who would trust you to cook their food?!"
                emir angry "Hey, I can cook! I make dinner for my family all the time!"
                you "Yeah, but I bet you put plastic flies in their ice cubes or unscrew the salt shaker or something."
                emir happy "Mayyyybe."
            "This quiz is dumb.":
                you "It's just a dumb quiz. Mr. Factor even said it's just for fun."
                emir "Okay, then what do you think you'll end up doing?"
                you "I guess I'll have to do something when I grow up... but I don't know what, yet."

    "Then the bell rang, and I could stop thinking about my future and just worry about getting to the next class."

    return
