# Town Map

label EnterMap:
    return

screen MapScreen():
    imagemap:
        auto "images/bg/townmap_%s.png"
        hotspot (1364, 640, 273, 263)       action [SetVariable("current_room", "Hallway"), Jump("ChangeRoom")]
        hotspot (179, 580, 376, 367)    action Jump("afterschool_gym")


        # TODO: fill in the rest of these if we actually use this map