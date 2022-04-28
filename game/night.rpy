# Night Events
# Night includes making dinner and going to bed
label get_event_night(curr_day):
    # TODO: Replace with cooking simulator???
    call meal_menu
        
    scene bedroom night
    "Then, I went to bed."
    return