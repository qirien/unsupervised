# After School Events
# After School includes clubs, hanging out at the park, etc


label afterschool_default:
    scene school
    # TODO: Replace with a cool map ?
    # call screen MapScreen

    $ which_event = "ryan"
    menu:
        "What should I do after school?"
        "Go to the Makerspace":
            $ which_event = "calvin"
        "Go to Cross Country":
            $ which_event = "emir"
        "Go to Drama Club":
            $ which_event = "nina"
        "Go to the climbing gym":
            $ which_event = "tabitha"
        "Go to the park":
            $ which_event = "ryan"

    $ next_event = get_next_event(which_event)
    call expression next_event

    "Then I went home."
    return
