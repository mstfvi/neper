# -*- coding: utf-8 -*-
import json
from random import randint

with open('data.json', encoding='utf8'):
    data = json.load(data_file)
JOKE_COUNT = len(data)


def get_joker():
    # Return random joke
    random_num = randint(1, JOKE_COUNT)
    joke = data[random_num]
    return joke.replace()
