# -*- coding: utf-8 -*-

__author__ = "Alexiy"

__date__ = "21.05.2018"

import random
import os

MIN_DELAY_TIME = 0.1
MAX_DELAY_TIME = 3.0
DELAY_DIFF = MAX_DELAY_TIME - MIN_DELAY_TIME

assert DELAY_DIFF > 0, 'Please, use valid constants'


def getNextStartTime():
    return random.random() * DELAY_DIFF + MIN_DELAY_TIME


def getUserName():
    return os.environ.get('USERNAME')


if __name__ == '__main__':
    import time

    name = getUserName()

    print 'let the game starts!'

    # make random real random
    random.seed(time.time())

    while True:
        # sleep current process
        time.sleep(getNextStartTime())

        startTime = time.time()
        data = raw_input('Go!\n')
        endTime = time.time()

        deltaTime = endTime - startTime

        if deltaTime != 0:
            score = len(data) / deltaTime
            print '{}, you score is {:2}'.format(name, score)
        else:
            print 'The cheater detected!'
            name = 'cheater'

        print 'Next round {}'.format(name)
        print 'Get ready {}'.format(name)
