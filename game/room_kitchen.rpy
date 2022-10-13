# Home Kitchen

label EnterKitchen:
    return

screen KitchenScreen():
    frame:
        background "kitchen"
        xfill True
        yfill True
        imagebutton:
            idle "gui/down_arrow.png"
            sensitive in_room 
            action [SetVariable("current_room", "Hallway"), Jump("ChangeRoom")]
            xalign 0.5
            yalign 0.9
            at alpha_imagebutton        
        imagebutton:
            idle "gui/right_arrow.png"
            sensitive in_room 
            action [SetVariable("current_room", "Livingroom"), Jump("ChangeRoom")]
            xalign 0.9
            yalign 0.5
            at alpha_imagebutton        

        # TODO: Add doing chores buttons