__author__ = 'dmitriy'

import time


def moop(i):
    time.sleep(1)


def poop():
    moop(2)
    time.sleep(2)
    moop(1)


def foo():
    bar()


def bar():
    bazz()
    something_random()


def bazz():
    time.sleep(.4)


def something_random():
    for i in xrange(100000):
        x = i + 1


def monkeys():
    time.sleep(3)
    moop(1)
    foo()


def run():
    poop()
    monkeys()
    moop(1)


if __name__ == "__main__":
    run()

