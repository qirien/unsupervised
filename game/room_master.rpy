# Home Master Bedroom

label EnterMasterBedroom:
    return

screen MasterBedroomScreen():
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

        # TODO: Add research on Mom's computer button