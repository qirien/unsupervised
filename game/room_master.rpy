# Home Master Bedroom

label EnterMasterBedroom:
    return

screen MasterBedroomScreen():
    style_prefix "room"
    frame:
        # TODO: different depending on time of day?
        background "master bedroom day"
        xfill True
        yfill True
        imagebutton:
            idle "gui/right_arrow.png"
            sensitive in_room
            action [SetVariable("current_room", "Hallway"), Jump("ChangeRoom")]
            xalign 0.9
            yalign 0.5
            at alpha_imagebutton

        # TODO: Look for Clues only after day 1
        # Actions for this room
        vbox:
            yalign 0.5
            xalign 0.5
            if ((day>=4) and (looked_for_clues == False)):
                textbutton "Look for Clues" action Call("research")
