import requests
import json
from telegram_path import *


def contests_list(gym):
    c = requests.get('http://codeforces.com/api/contest.list?gym=' + str(gym).lower())
    contests_data = json.loads(c.text)
    if contests_data['status'] == 'FAILED':
        fail("Too many requests")
    return contests_data['result']


def user_rating(handle):
    r = requests.get('http://codeforces.com/api/user.rating?handle=' + handle)
    rating_data = json.loads(r.text)
    if rating_data['status'] == 'FAILED':
        fail("Too many requests")
    return rating_data['result']
