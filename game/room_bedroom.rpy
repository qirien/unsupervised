# Home Bedroom

label EnterBedroom:
    return

screen BedroomScreen():
    frame:
        # TODO: different depending on time of day?
        background "bedroom"
        xfill True
        yfill True
        imagebutton:
            idle "gui/left_arrow.png"
            sensitive in_room 
            action [SetVariable("current_room", "Hallway"), Jump("ChangeRoom")]
            xalign 0.1
            yalign 0.5
            at alpha_imagebutton
        textbutton "Play video games" action [Call("videogames"), Return("Bedroom")]  #TODO: this causes an error on return
        #textbutton "Do Homework" action Call("homework")

        # TODO: Add playing video games, doing homework buttons