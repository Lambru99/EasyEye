#!/usr/bin/env python
from beeply import notes
import time


def sound_to_stop():
    mybeep = notes.beeps(900)
    mybeep.hear('E')
    mybeep.hear('C')
    mybeep.hear('E')
    mybeep.hear('C')


def sound_to_start():
    myfirstbeep = notes.beeps(1500)
    myfirstbeep.hear('A')


def start(concentration, waiting):
    minutes = 0
    waiting_time = 0
    while minutes != concentration:
        print("minute of concentration: " + str(minutes))
        time.sleep(60)
        minutes = minutes + 1

    minutes = 0
    sound_to_stop()
    while waiting_time != waiting:
        print("minute of waiting: " + str(waiting_time))
        time.sleep(60)
        waiting_time = waiting_time + 1
    waiting_time = 0
    sound_to_start()


def loop_start():
    global concentration, waiting
    try:
        concentration = (int)(input("Please enter how long you want to stay focused"
                                    "\n(This program accepts a value written in minutes) :"))
        waiting = (int)(input("Please enter how long you want to wait"
                              "\n(This program accepts a value written in minutes):"))
    except ValueError:
        print("!ERROR! Type an integer number!")
        loop_start()
    while 0 == 0:
        start(concentration, waiting)


if __name__ == "__main__":
    loop_start()
