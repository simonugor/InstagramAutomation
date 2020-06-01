#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import time
from login import *
from help import *
from follow import *
from stats import *
from settime import *
from follow_likers import *

app = Flask(__name__)

saved_username = ""
saved_password = ""
saved_time = "60" #use this as a parameter to follow function to set value of time.sleep(this value) between follows

@app.route("/")
def index():
    message1 = "Your server is running! Welcome to the Instabot API."
    message2 = "Use [GET] /help method to see all commands."
    return jsonify(message1, message2)

#/help
@app.route("/help", methods=["GET"])
def get_help():
    help = send_help()
    if help != None:
        return jsonify(help)
    else:
        return jsonify("Something went wrong, please try to realunch the program.")

#/set_time - use this to set intervals between actions
@app.route("/set_time", methods=["POST"])
def set_time():
    time = request.args.get('time')
    setting =  time_setting(time)
    if setting != None:
        message_to_return = str(setting)
        global saved_time
        saved_time = message_to_return
        return jsonify("Interval between actions was succesfully set to: " + message_to_return + " seconds")
    else:
        return jsonify("Something went wrong")

#/login
@app.route("/login", methods=["POST"]) #implement checking if login was succesful!! Opening DMs for example
def login_instagram():
    username = request.args.get('username')
    password = request.args.get('password')
    global saved_username
    saved_username = username
    global saved_password
    saved_password = password
    if username != None and password != None:
        function = login(username, password)
    else:
        return jsonify("Please enter username and password")
    if function == True:
        message1 = "Login succesful. Your login data has been saved."
        message2 = "To delete your login data please use [POST] /delete"
        return jsonify(message1, message2)
    elif function == False:
        return jsonify("Login failed. Make sure your username and password were entered correctly.")

#/delete to delete saved username and password
@app.route("/delete", methods=["POST"])
def delete_data():
    global saved_username
    saved_username = ""
    global saved_password
    saved_password = ""
    return jsonify("You login data has been succesfully deleted.")

#/print_data only used for testing purposes
@app.route("/print_data", methods=["POST"])
def print_data():
    time = str(saved_time) + " seconds"
    return jsonify(saved_username, saved_password, time)

#/follow_followers
@app.route("/follow_followers", methods=["POST"]) #file called follow.py
def follow_followers():
    account = request.args.get('account')
    amount = request.args.get('amount')
    if saved_time != "":
        if amount != None and int(amount) != 0:
            following = log_into_account(saved_username, saved_password, account, int(saved_time), int(amount))
            if following == False:
                return jsonify("Something went wrong.")
            elif following == "toomanyaccounts":
                return jsonify("Your amount of accounts is too big, please enter smaller number")
            else:
                return jsonify("Successfully followed " + str(amount) + " users.")
        elif amount == None:
            return jsonify("Please enter amount of accounts you would like to follow.")
        elif int(amount) == 0:
            return jsonify("Amount of accounts to follow cannot be 0!")
    elif saved_time == "":
        return jsonify("Please before using this function use [POST] /set_time (with parameter 'time' in minutes")
    else:
        return jsonify("I reaaally messed something up")

#/follow_likers
@app.route("/follow_likers", methods=["POST"]) #file called follow_likers.py
def follow_likers():
    username = saved_username
    password = saved_password
    account = request.args.get('account')
    amount = request.args.get('amount')
    time = saved_time
    if time != "":
        if amount != None and int(amount) != 0:
            following_likers = login_follow_likers(username, password, account, int(time), int(amount))
            if following_likers == False:
                return jsonify("Something went wrong")
            elif following_likers == "toomanyaccounts":
                return jsonify("Your amount of accounts is too big, please enter smaller number")
            else:
                return jsonify("Successfully followed " + str(amount) + " users.")
        elif amount == None:
            return jsonify("Please enter amount of accounts you would like to follow.")
        elif int(amount) == 0:
            return jsonify("Amount of accounts to follow cannot be 0!")
    elif saved_time == "":
        return jsonify("Please before using this function use [POST] /set_time (with parameter 'time' in minutes")
    else:
        return jsonify("I reaaally messed up")

#/stats
@app.route("/stats", methods=["GET"])
def stats():
    func_login = log_into_account_stats(saved_username, saved_password)
    if func_login == False:
        return jsonify("Something went wrong")
    elif func_login == "account_not_found":
        return jsonify("Account you are looking for was not found!")
    elif func_login != False and func_login != None:
        return jsonify(func_login)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers[
        'Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE"
    return response


if __name__ == "__main__":
    app.run(debug=False, port=8888)
