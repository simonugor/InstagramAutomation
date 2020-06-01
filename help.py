def send_help():
    message = "Please make sure you use [POST] /login function first!"
    message1 = "Here are all commands you can use after using /login function:"
    message2 = "[POST] /delete -> deletes saved login data"
    message3 = "[POST] /set_time (parameter: time *in minutes*) -> sets time between follow actions (set to 10min by default"
    message4 = "[POST] /print_data -> returns your username, password and time set between actions"
    message5 = "[GET] /stats -> returns stats about your account (account you logged in with)"
    message6 = "[POST] /follow_followers (parameters: account, amount) -> follows given amount of users followin given account"
    message7 = "[POST] /follow_likers (parameters: account, amount) -> follows given amount of users that liked recent post of given account"
    return message, message1, message2, message3, message4, message5, message6, message7