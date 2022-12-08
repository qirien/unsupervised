# Home Hallway

label EnterHallway:
    return

screen HallwayScreen():
    style_prefix "room"
    frame:
        background "house hallway"
        xfill True
        yfill True
        imagebutton:
            idle "gui/up_arrow.png"
            sensitive in_room
            action [SetVariable("current_room", "Map"), Jump("ChangeRoom")]
            xalign 0.5
            yalign 0.1
            at highlight_imagebutton
        imagebutton:
            idle "gui/down_arrow.png"
            sensitive in_room
            action [SetVariable("current_room", "Kitchen"), Jump("ChangeRoom")]
            xalign 0.5
            yalign 0.9
            at highlight_imagebutton
        imagebutton:
            idle "gui/right_arrow.png"
            sensitive in_room
            action [SetVariable("current_room", "Bedroom"), Jump("ChangeRoom")]
            xalign 0.9
            yalign 0.5
            at alpha_imagebutton
        imagebutton:
            idle "gui/left_arrow.png"
            sensitive in_room
            action [SetVariable("current_room", "MasterBedroom"), Jump("ChangeRoom")]
            xalign 0.1
            yalign 0.5
            at alpha_imagebutton

        # TODO: Add use phone button on Mom's purse? or have phone icon all the time in adventure mode? Show current time?
