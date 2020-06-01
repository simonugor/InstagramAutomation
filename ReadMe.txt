Dear Mr. Deepak, 

this is my Instagram Automation project for Programming.

Because this is pretty niche specific program that is not for everyone, let me give you a quick walkthrough so you know how to use it.

First of all, like I've stated in my proposal, this is not a bot. My program will actually do things over real time so Instagram doesn't get us blocked. I am using chromedriver version 83 and it needs to match version of Google Chrome version 83. If you are using different version of Chrome browser, please download matching version of chromedriver here: https://chromedriver.chromium.org/downloads and replace the version  of chromedriver given in my folder.

I created a short video to how to use my program, if you have time please watch it so you get the idea of how it works and don't have to read the users manual below: https://www.dropbox.com/s/6ljpplzloaoyvkm/Programming.mp4?dl=0

Quick Users Manual:

1. First run the api.py file and try http://127.0.0.1:8888/ if server is up and running

2. You will be first required to use [POST] /login function with parameters username and password to log in into Instagram. For testing purposes I've borrowed this Instagram account you can use:
			username: hyped_combat_
			password: 123testing123

3. With function [POST] /set_time with parameter time (in minutes) you can set how long will the program wait between follow actions. I've set it by default to 1 minute so you don't have to wait ages to test my program. Please at this point don't set too many follow actions because Instagram can get us blocked. If you want to see my program work on a long term, please set time to at least 5 minutes between follow actions.

4. To test my program you can choose between [POST] /follow_followers and [POST] 
/follow_likers both requiring parameters account and amount. Account meaning from which account will my program get and follow users, amount meaning how many users will it follow. We can use Instagrams official account for testing purposes. Here is how it works:
			account: instagram
			amount: 2

Please be patient, I'm trying to do everything like real human would do it so its not suspicious for Instagram checking for bots. Scrolling through users to load enough usernames may take a while. PLEASE DO NOT CLOSE THE BROWSER MANUALLY, IT WILL CLOSE ITSELF WHEN DONE. 

First it will get the usernames, open the first one and hit the follow button. After following the first one it will wait time set by us (1 minute in this case) before opening and following another user. If you would like to see more information about what my program is doing, you can always check python terminal while running, where I'm printing out basic actions.
