# Home Living Room

label EnterLivingroom:
    return

screen LivingroomScreen():
    style_prefix "room"
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

        # Actions for this room
        vbox:
            yalign 0.5
            xalign 0.5
            textbutton "Watch a show" action Call("tv") # TODO: for some reason these change background to bedroom, but kitchen events don't?!
            textbutton "Read a book" action Call("read")
