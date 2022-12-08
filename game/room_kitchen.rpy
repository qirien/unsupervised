# Home Kitchen

label EnterKitchen:
    return

screen KitchenScreen():
    style_prefix "room"
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

        # Actions for this room
        vbox:
            yalign 0.5
            xalign 0.5
            textbutton "Eat something" action Call("meal_menu")
            textbutton "Clean up" action Call("clean")
