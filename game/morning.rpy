# Morning Class Events
# Morning classes include advisory (Emir), gym, math (Calvin), social studies
label get_event_morning(curr_day):
    scene classroom
    "Advisory, gym, math, social studies... I went to class like a good little robot."
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
    $ career_pts = {"R":0, "I":0, "A":0, "S":0, "E":0, "C":0}
    # R ealistic, practical, doers
    # I deas, intellectual
    # A rtistic, expressive
    # S ocial, helpers, teachers
    # E nterprising, working with people and data
    # C onventional, working with data and rules
    # from Holland Codes, a taxonomy of interests, https://en.wikipedia.org/wiki/Holland_Codes
    
    default morning_14_set1 = set()
    default morning_14_set2 = set()
    default morning_14_set3 = set()
    default morning_14_set4 = set()    
    label morning_14_career1:
        if (len(morning_14_set1) >= 3):
            jump morning_14_career2
        menu:        
            set morning_14_set1
            "I would rather be..."
            "Making something useful":
                $ career_pts["R"] += 1
                jump morning_14_career1
            "Thinking about how to make something":
                $ career_pts["I"] += 1       
                jump morning_14_career1 
            "Making something look beautiful":
                $ career_pts["A"] += 1
                jump morning_14_career1
            "Making something that helps someone":
                $ career_pts["S"] += 1
                jump morning_14_career1
            "Leading a group to make something":
                $ career_pts["E"] += 1
                jump morning_14_career1
            "Following instructions to make something":
                $ career_pts["C"] += 1
                jump morning_14_career1

    label morning_14_career2:
        if (len(morning_14_set2) >= 3):
            jump morning_14_career3
        menu:
            set morning_14_set2
            "In a zombie apocalypse, I would probably be..."        
            "In the middle of the action.":
                $ career_pts["R"] += 1
                jump morning_14_career2
            "Studying the best survival techniques.":
                $ career_pts["I"] += 1       
                jump morning_14_career2 
            "Keeping up morale.":
                $ career_pts["A"] += 1
                jump morning_14_career2
            "Running a school or clinic.":
                $ career_pts["S"] += 1
                jump morning_14_career2
            "The leader helping everyone see the big picture":
                $ career_pts["E"] += 1
                jump morning_14_career2
            "Keeping everything organized.":
                $ career_pts["C"] += 1
                jump morning_14_career2

    label morning_14_career3:
        if (len(morning_14_set3) >= 3):
            jump morning_14_career4
        menu:
            set morning_14_set3
            "If I worked at a school, I would be..."        
            "A PE/computer/shop teacher":
                $ career_pts["R"] += 1
                jump morning_14_career3
            "A science teacher":
                $ career_pts["I"] += 1       
                jump morning_14_career3 
            "An art/music/drama teacher.":
                $ career_pts["A"] += 1
                jump morning_14_career3
            "The school nurse/counselor":
                $ career_pts["S"] += 1
                jump morning_14_career3
            "The principal":
                $ career_pts["E"] += 1
                jump morning_14_career3
            "A librarian or math teacher":
                $ career_pts["C"] += 1
                jump morning_14_career3          
    
    label morning_14_career4:
        if (len(morning_14_set4) >= 3):
            jump morning_14_career5
        menu:
            set morning_14_set4
            "If I have to do chores I dislike, I'm most likely to..."
            "Just jump in and start working.":
                $ career_pts["R"] += 1
                jump morning_14_career4
            "Study cleaning chemicals and choose the best method.":
                $ career_pts["I"] += 1       
                jump morning_14_career4 
            "Put on some good music or sing while I work.":
                $ career_pts["A"] += 1
                jump morning_14_career4
            "Think about how much I'm helping my family while I work.":
                $ career_pts["S"] += 1
                jump morning_14_career4
            "Persuade a friend to help me.":
                $ career_pts["E"] += 1
                jump morning_14_career4
            "Make a list first and enjoy checking off each item.":
                $ career_pts["C"] += 1
                jump morning_14_career4 
    
    label morning_14_career5:
        "Okayyyyy, that was kind of a weird test."

        # Pop off the three smallest ones and we're left with the three most chosen options.
        $ career_pts.pop(min(career_pts))
        $ career_pts.pop(min(career_pts))
        $ career_pts.pop(min(career_pts))

        $ career_desc = "You like:\n"
        if "R" in career_pts:
            $ career_desc += "things that are practical and realistic\n"
        if "I" in career_pts:
            $ career_desc += "thinking about ideas and understanding concepts\n"
        if "A" in career_pts:
            $ career_desc += "being creative and artistic\n"
        if "S" in career_pts:
            $ career_desc += "helping or teaching people\n"
        if "E" in career_pts:
            $ career_desc += "leading and persuading people\n"
        if "C" in career_pts:
            $ career_desc += "structure, order, and organization\n"
        $ career_desc = career_desc.rstrip()
        quiz "[career_desc]"
        $ career_desc = "You should think about careers such as:\n"



    return
