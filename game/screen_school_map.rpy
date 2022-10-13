screen school_map:
    imagemap:
        auto "images/bg/schoolmap_%s.png"
        hotspot (747,335,105,220)       action Return("103")
        hotspot (22,336,438,114)        action Return("the Makerspace")
        hotspot (888, 468, 455, 245)    action Return ("the library")
        hotspot (885, 336, 457, 132)    action Return ("the computer lab")
        hotspot (886, 37, 465, 257)     action Return ("the cafeteria")
        hotspot (1384, 107, 407, 181)   action Return ("the theatre")
        hotspot (1385, 335, 408, 138)   action Return ("the music rooms")
        hotspot (1382, 516, 201, 148)   action Return ("the art room")
        hotspot (1585, 516, 205, 148)   action Return ("the woodshop")
        hotspot (1382, 708, 408, 275)   action Return ("the gym")
        hotspot (887, 716, 456, 91)     action Return ("the office")
        hotspot (748, 691, 103, 218)    action Return ("101")
        hotspot (747, 557, 105, 133)    action Return ("102")
        hotspot (496, 798, 209, 113)    action Return ("111")

        # TODO: fill in the rest of these if we actually use this map