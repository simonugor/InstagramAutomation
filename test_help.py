import unittest
from help import send_help
from login import login

#Here is the basic idea of testing for my program. I just wanted to show you that I understad this concept.

#messages that should be returned from send_help() function
messages = ('Please make sure you use [POST] /login function first!',
 'Here are all commands you can use after using /login function:',
 '[POST] /delete -> deletes saved login data',
 '[POST] /set_time (parameter: time *in minutes*) -> sets time between follow '
 'actions (set to 10min by default',
 '[POST] /print_data -> returns your username, password and time set between '
 'actions',
 '[GET] /stats -> returns stats about your account (account you logged in '
 'with)',
 '[POST] /follow_followers (parameters: account, amount) -> follows given '
 'amount of users followin given account',
 '[POST] /follow_likers (parameters: account, amount) -> follows given amount '
 'of users that liked recent post of given account')


#test class
class TestHelp(unittest.TestCase):

    #testing send_help()
    def test_help(self):
        self.assertEqual(send_help(), messages) #should return messages

    #testing login(username, password) - will run the browser and test inserting empty parameters
    def test_login(self):
        self.assertEqual(login("", ""), False) #with username and password empty, login() should return False