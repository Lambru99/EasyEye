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


def start():
    minuti = 0
    attesa = 0
    while minuti != 60:
        print("minuti: " + str(minuti))
        time.sleep(60)
        minuti = minuti + 1

    minuti = 0
    sound_to_stop()
    while attesa != 15:
        print("attesa: " + str(attesa))
        time.sleep(60)
        attesa = attesa + 1
    attesa = 0
    sound_to_start()


def loop_start():
    while 0 == 0:
        start()


if __name__ == "__main__":
    loop_start()
