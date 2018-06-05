# Concurrent Programming Assignment

## Intro
In this  assignment,  you are  asked  to  simulate  two  different  types of  queuing  systems  found  in newfoundland, namely: queue is Tim Hortons and queue in Dominion.

The first queue should be implemented in a class called TimQueue and is modeled after the lineup procedure found in most Tim Hortons in St. John’s. In such a queue, there is only one lineup and multiple server station for  serving for the customers on that line. After servicing a customer from a service station, the server comes back to the serving station and serve the next customer on the line. All servers are run in parallel.  

The second type of queue should be implemented in a class called DominionQueue, which is modeled after the customer checkout queue system in the popular grocery store Dominion in St. John’s. Here we have multiple checkout station in the store and each checkout station has its own queue. When a new customer proceed to checkout, it is the customers choice to select a queue among the available ones. For this assignment you can consider, the customer will always select the queue that has the lowest number of customer waiting. If there are multiple queue with lowest number of customer waiting, the new customer can choose one randomly.  

## Usage

`python main.py -q < tim || dominion> -n <time to run simulation>`

## Results
### Tim Hortons (4 simulated hours) - 2 Registers, Max line of 6
Customers Arrived: 177

Customers Served: 77

Customers Turned Away: 93

Average Time Taken to Serve each customer: 187.1818181818182

Average Time Taken for complete service: 1300.1298701298701

### Dominion (4 simulated hours) - 3 Registers, Max line of 2
Customers Arrived: 183

Customers Served: 115

Customers Turned Away: 61

Average Time Taken to Serve each customer: 125.6608695652174

Average Time Taken for complete service: 1010.2086956521739

