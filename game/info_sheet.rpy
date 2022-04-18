screen info_sheet():
    default about_me_field = "name"
    frame:
        vbox:
            label "About Me"
            hbox:
                text "This paper is by "
                if (about_me_field == "name"):
                    input value VariableInputValue("your_name")
                else:
                    textbutton "[your_name]" action SetScreenVariable("about_me_field", "name")

            hbox:
                text "[your_name]"
                text " likes to "
                if (about_me_field == "hobby"):
                    input value VariableInputValue("hobby")
                else:
                    textbutton "[hobby]" action SetScreenVariable("about_me_field", "hobby")

            hbox:
                text "and "
                textbutton "[her_his]" action ToggleGender()
                text " favorite food is "
                if (about_me_field == "food"):
                    input value VariableInputValue("favorite_food")
                else:
                    textbutton "[favorite_food]" action SetScreenVariable("about_me_field", "food")

            hbox:
                text "Also, [your_name] hates it when teachers "
                if (about_me_field == "hated"):
                    input value VariableInputValue("hated_action")
                else:
                    textbutton "[hated_action]" action SetScreenVariable("about_me_field", "hated")

            textbutton "All Done" action Return()


init python:
    def toggle_gender():
        global her_his, she_he, her_him
        if (her_his == "her"):
            her_his = "his"
            she_he = "he"
            her_him = "him"
        elif (her_his == "his"):
            her_his = "their"
            she_he = "they"
            her_him = "them"
        else:
            her_his = "her"
            she_he = "she"
            her_him = "her"
        renpy.restart_interaction()
        return

    ToggleGender = renpy.curry(toggle_gender)


