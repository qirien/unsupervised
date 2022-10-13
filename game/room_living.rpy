# Home Living Room

label EnterLivingroom:
    return

screen LivingroomScreen():
    frame:
        # TODO: different depending on time of day?
        background "living"
        xfill True
        yfill True
        imagebutton:
            idle "gui/left_arrow.png"
            sensitive in_room 
            action [SetVariable("current_room", "Kitchen"), Jump("ChangeRoom")]
            xalign 0.1
            yalign 0.5
            at alpha_imagebutton            

        # TODO: Add watch TV button, housework button