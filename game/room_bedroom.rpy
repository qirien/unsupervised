# Home Bedroom

label EnterBedroom:
    return

screen BedroomScreen():
    style_prefix "room"
    frame:
        # TODO: different depending on time of day?
        background "bedroom day"
        xfill True
        yfill True
        imagebutton:
            idle "gui/left_arrow.png"
            sensitive in_room
            action [SetVariable("current_room", "Hallway"), Jump("ChangeRoom")]
            xalign 0.1
            yalign 0.5
            at alpha_imagebutton

        # Actions for this room
        vbox:
            yalign 0.5
            xalign 0.5
            textbutton "Play video games" action Call("videogames")
            textbutton "Do Homework" action Call("homework")
