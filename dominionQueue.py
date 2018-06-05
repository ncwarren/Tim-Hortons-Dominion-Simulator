#!/usr/bin/env python

'''
 Nick Warren - #201404779
 Concurrent Programming Assignment #2
 DominionQueue Implementation file
 multiple checkout stations running in parallel, each having their own queue
'''
from dominionServer import ServerStation
from customer import Customer
from threading import Thread

class DominionQueue():
    def __init__(self, servingStationCount, queueLimit, clock):
        # self.lineup = queue.Queue(queueLimit)
        self.servingStationCount = servingStationCount
        self.clock = clock
        self.customers = []

        # Init a number of threads running as a server station
        self.servingStations = []
        for i in range(0, servingStationCount):
            print("Creating serving station {}".format(i))
            station = ServerStation(self, queueLimit)
            station.start()
            self.servingStations.append(station)


    def customerArrived(self, timeNow):
        newCustomer = Customer(timeNow)
        self.customers.append(newCustomer)
        placedInLine = False

        # Find the length of the shortest line
        shortestLineLen = 100
        shortestLine = None
        for station in self.servingStations:
            if station.lineup.full() == False:
                if shortestLineLen > station.lineup.qsize():
                    shortestLineLen = station.lineup.qsize()
                    shortestLine = station

        # Join the shortest line if avaliable, if not wait up to 20 seconds
        if shortestLine != None:
            shortestLine.lineup.put(newCustomer)
            placedInLine = True
            print("Customer placed in line (less than max)")
        else:
            waitUntil = timeNow + 20
            print("Customer waiting for queue enterance")
            while(waitUntil >= self.clock.timeSinceInit):
                for station in self.servingStations:
                    if station.lineup.full() == False:
                        station.lineup.put(newCustomer)
                        placedInLine = True

        if placedInLine == False:
            newCustomer.turnedAway()

    def closeShop(self):
        for station in self.servingStations:
            station.closeShop()
        del self

    def printStats(self):
        served = 0
        turnedAway = 0
        averageTime = 0
        averageTotal = 0

        for customer in self.customers:
            if customer.wasTurnedAway == True:
                turnedAway += 1
            if customer.served == True:
                served += 1
                averageTotal += customer.timeToBeServed
        averageTime = self.clock.timeSinceInit/served
        averageTotal = averageTotal/served

        print("--Stats for Simulation--")
        print("Customers Arrived: {}".format(len(self.customers)))
        print("Customers Served: {}".format(served))
        print("Customers Turned Away: {}".format(turnedAway))
        print("Average Time Taken to Serve each customer: {}".format(averageTime))
        print("Average Time Taken for complete service: {}".format(averageTotal))
