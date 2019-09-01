import time

from codeforces_path import *
from time_checking import *


def get_round_statistics(x):
    send_msg(x['contestName'] + ', Место ' + str(x['rank']) + ', ' + str(x['oldRating']) + ' -> ' + str(x['newRating']))


def get_round_notification(x):
    time_before = x['relativeTimeSeconds']
    send_msg(x['name'] + " " + str(time_before_round(time_before)))


def monitoring():
    know = 0
    while True:
        contests = contests_list(False)
        contests_before = list(filter(lambda x: x['phase'] == 'BEFORE', contests))
        contest_is_running = any(map(lambda x: x['phase'] == 'CODING' and x['type'] == 'CF', contests))
        for i in contests_before:
            time_before = i['relativeTimeSeconds']
            if not contest_is_running and need_post(time_before):
                get_round_notification(i)
        rating = user_rating('CodeWeakness')
        for i in range(know, len(rating)):
            get_round_statistics(rating[i])
        know = len(rating)
        time.sleep(0.2)
