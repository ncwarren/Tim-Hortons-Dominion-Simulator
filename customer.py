#!/usr/bin/env python

'''
 Nick Warren - #201404779
 Concurrent Programming Assignment #2
 Customer Object
 Customer Object with attributes for storing information related to times
'''

class Customer():

    def __init__(self, timeInitalized):
        self.timeArrived = timeInitalized
        self.timeToBeServed = None
        self.wasTurnedAway = False
        self.served = False

    def customerServed(self, timeNow):
        self.timeToBeServed = timeNow - self.timeArrived
        self.served = True

    def turnedAway(self):
        self.wasTurnedAway = True
