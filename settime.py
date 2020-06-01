def time_setting(time_in_minutes):
    minutes = int(time_in_minutes)
    time_in_seconds = minutes * 60
    #rounding just in case
    time_in_seconds_rounded = round(time_in_seconds)
    return time_in_seconds_rounded
