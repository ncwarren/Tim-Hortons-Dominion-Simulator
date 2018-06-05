#!/usr/bin/env python

'''
 Nick Warren - #201404779
 Concurrent Programming Assignment #2
 Main file for launching Tim Hortons & Dominion Queue Simulations with multithreading
 '''

from argparse import ArgumentParser
import random
import threading

from timQueue import TimQueue
from dominionQueue import DominionQueue
from simulatedClock import SimulatedClock
from customer import Customer

if __name__ == '__main__':
    print("Booting...")
    parser = ArgumentParser()
    parser.add_argument("-q", "--queue", dest="queueOption",
                    help="tim or dominion to pick which simulation to run",
                    metavar="QUEUE")
    parser.add_argument("-n", "--numSec", dest="numberOfSec",
                help="Length of simulated seconds to run simulator",
                metavar="LENGTH")

    args = parser.parse_args()
    timeRunUntil = int(args.numberOfSec)

    # Create clock on seperate thread
    clock = SimulatedClock()
    clock.start()

    # Boot either simulation as per argument
    if args.queueOption == "tim":
        print('Booting Tim Horton Queue')
        instance = TimQueue(2,6, clock)
    elif args.queueOption == "dominion":
        instance = DominionQueue(3,2,clock)
        print('Booting Dominion Queue')
    else:
        print("Unknown Boot Request")

    # Add customers to store
    lastCustomerTime = 0
    while clock.timeSinceInit < timeRunUntil :
        randNum = random.randint(40,121)
        customerArrived = False
        while(customerArrived == False):
            timeNow = clock.timeSinceInit
            if timeNow - lastCustomerTime > randNum: # Add a new customer every 40 - 120 sec
                print("Customer Arrived")
                print("Time left: {}".format(timeRunUntil - clock.timeSinceInit))
                instance.customerArrived(timeNow)
                customerArrived = True
                lastCustomerTime = timeNow

    print("Times up!")
    instance.printStats()
    instance.closeShop()
