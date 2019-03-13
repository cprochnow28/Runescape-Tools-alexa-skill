from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import request
import time
from time import gmtime, strftime
import unidecode

app = Flask(__name__)
ask = Ask(app, "/")

def get_timeUntil():
    currentHour = int(strftime("%-H", gmtime()))
    day = strftime("%A", gmtime())


    if (day == "Sunday"):
        if (currentHour < 5):
            return calc_timeUntil(5)
        if (currentHour < 12):
            return calc_timeUntil(12)
        if (currentHour < 19):
            return calc_timeUntil(19)
        else:
            return calc_timeUntil(26)

    if (day == "Monday"):
        if (currentHour < 2):
            return calc_timeUntil(2)
        if (currentHour < 9):
            return calc_timeUntil(9)
        if (currentHour < 16):
            return calc_timeUntil(16)
        else:
            return calc_timeUntil(23)

    if (day == "Tuesday"):
        if (currentHour < 6):
            return calc_timeUntil(6)
        if (currentHour < 13):
            return calc_timeUntil(13)
        if (currentHour < 20):
            return calc_timeUntil(20)
        else:
            return calc_timeUntil(30)

    if (day == "Wednesday"):
        if (currentHour < 3):
            return calc_timeUntil(3)
        if (currentHour < 10):
            return calc_timeUntil(10)
        if (currentHour < 17):
            return calc_timeUntil(17)
        else:
            return calc_timeUntil(24)

    if (day == "Thursday"):
        if (currentHour < 7):
            return calc_timeUntil(7)
        if (currentHour < 14):
            return calc_timeUntil(14)
        if (currentHour < 21):
            return calc_timeUntil(21)
        else:
            return calc_timeUntil(28)



    if (day == "Friday"):
        if (currentHour < 4):
            return calc_timeUntil(4)
        if (currentHour < 11):
            return calc_timeUntil(11)
        if (currentHour < 18):
            return calc_timeUntil(18)
        else:
            return calc_timeUntil(25)


    if (day == "Saturday"):
        if (currentHour < 1):
            return calc_timeUntil(1)
        if (currentHour < 8):
            return calc_timeUntil(8)
        if (currentHour < 15):
            return calc_timeUntil(15)
        if (currentHour < 22):
            return calc_timeUntil(22)
        else:
            return calc_timeUntil(29)


def calc_timeUntil(nextHour) :
    currentHour = int(strftime("%-H", gmtime()))
    currentMinute = int(strftime("%-M", gmtime()))

    msgPart1 = "You have "
    msgPart2 = " hours and "
    msgPart3 = " minutes until the next warbands"

    hoursLeft = str((nextHour-1) - currentHour)
    minutesLeft = str(59 - currentMinute)
    completeMsg = msgPart1 + hoursLeft + msgPart2 + minutesLeft + msgPart3
    return completeMsg



@app.route('/')
def homepage():
    return "hi there, how ya doin?"

@ask.launch
def start_skill():
    welcome_message = "I'm currently tracking the where abouts of a warband camp"
    return question(welcome_message)

@ask.intent("timeUntilIntent")
def share_time_left():
    timeLeft = get_timeUntil()
    return statement(timeLeft)


@ask.intent("AMAZON.HelpIntent")
def usage():
    return question("Try asking me........ When is warbands... or ..... when is the next warbands going to happen")

@ask.intent("AMAZON.StopIntent")
def stopFunction():
    return statement("I got camps to track anyways")

@ask.intent("AMAZON.CancelIntent")
def cancelFunction():
    return statement("I got camps to track anyways, good luck adventurer")


if __name__ == '__main__':
    app.run(debug=True)
