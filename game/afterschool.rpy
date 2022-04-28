# After School Events
# After School includes clubs, hanging out at the park, etc
label get_event_afterschool(curr_day):
    scene school
    # TODO: Replace with a cool map 
    menu:
        "What should I do after school?"
        "Go to the Makerspace":
            "I hung out at the Makerspace and worked on my project."
        "Go to Cross Country":
            "I ran and ran and ran."
        "Go to Drama Club":
            "We played some improv games and practiced a song."
        "Go to the climbing gym":
            "I climbed some easy walls and tried some hard bouldering problems."
        "Go to the park":
            "I rode my bike around and stopped at the park to chase some pigeons."
        
    "Then I went home."
    return
