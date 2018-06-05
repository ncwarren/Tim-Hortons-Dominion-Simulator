#!/usr/bin/env python

'''
 Nick Warren - #201404779
 Concurrent Programming Assignment #2
 Simulated Clock

'''
from time import sleep
from threading import Thread

class SimulatedClock(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.timeSinceInit = 0
        self.active = True

    def run(self):
        print("Clock started")
        while(self.active == True):
            sleep(0.001)
            self.timeSinceInit += 1


    def retireThread(self):
        self.active = False
