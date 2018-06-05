#!/usr/bin/env python

'''
 Nick Warren - #201404779
 Concurrent Programming Assignment #2
 ServerStation for DominionQueue
 Server capable of serviging a single customer at a time with their own queue
'''
import random
import queue
from threading import Thread

class ServerStation(Thread):

    def __init__(self, timQueue, queueLimit):
        ''' Constructor. '''
        self.active = True
        self.lineup = queue.Queue(queueLimit)
        self.busy = False
        self.clock = timQueue.clock

        Thread.__init__(self)


    def run(self):
        while(self.active) :
            currentCustomer = self.lineup.get()
            print("Serving customer")
            self.busy = True
            timeStartedJob = self.clock.timeSinceInit
            randNum = random.randint(120,601)
            timeFinishJob = timeStartedJob + randNum
            while(self.clock.timeSinceInit < timeFinishJob):
                pass
            currentCustomer.customerServed(timeFinishJob)
            self.busy = False


    def closeShop(self):
        self.active = False
