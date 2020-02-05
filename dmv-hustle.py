"""
# DMV Hustle

## Problem Description

The Department of Motor Vehicles is one of the busiest places in the United State. 
You will find people standing in a long queue to get a Drivers License, 
register their vehicles, etc.  Officials of the DMV want to improve this process. 
In order to do so, they want to know the total number of customers successfully 
served in a day and the number of customers that are served at each window.


This information will help officials determine if they need to open more windows 
and/or increase the size of the queue. You have been asked to build a simple 
tool that would help DMV officials collect this information from historical 
customer arrival data.


## Guidelines


### Inputs

    - Number of windows availabe to serve customers
    - Maximum size of the queue (Maximum number of customers that can wait in the queue)
    - Historical customer arrival data (sorted by arrival timestamp)


### Output

    - How many customers were successfully served by the DMV?
    - How many customers were served at each window?


### Format of Historical Customer Arrival Data

The input is an array of strings representing historical customer data 
(sorted by arrival timestamp) each with the format `<arrivalTimestamp>`, 
`<serviceTime>`, `<toleranceTime>`.


    - `<arrivalTimestamp>` is a non-negative integer representing the second at which 
        the customer arrived
    - `<serviceTime>` is a positive integer representing the time duration needed 
        for serving this customer
    - `<toleranceTime>` is a positive integer representing the time duration the customer 
        can wait in the queue since they arrived. After this time elapses, the customer 
        will drop out from the queue and go home.


### Customer Lifecycle at DMV


    - A customer arrives at a specific time `arrival Timestamp` to the DMV and requires 
        `serviceTime` seconds for serving them
    - If there are free windows available when the customer arrived, they can directly 
        go to the first available window for getting served and the particular window 
        becomes busy for the next `serviceTime` seconds
    - If all the windows are busy, the customer must wait in the queue until a window 
        becomes available and all the customers who are already waiting in the queue 
        are served
    - DMV queue has a limited capacity and can hold only up to a specific number of 
        customers. If the queue reaches its capacity, it cannot take up any new customers 
        and they will have to go home without being served
    - A customer also has a tolerance time `toleranceTime` seconds, which is the time 
        duration they can spend waiting in the queue since arrival. If the customer is 
        not assigned to a window within the tolerance time, they will become unhappy and 
        go home
    <br>


## Interface
Implement the following method: 
``` def solution(A, Y, Z)```
Given:
- an array of strings that represent customers (denoted by `A` in the method) representing arrival data for `numCustomers` customers
- an integer `numWindows` (denoted by `Y`) representing the number of windows for serving customers 
- an integer `queueSize` (denoted by `Z`) representing the size of the DMV queue
Return:
- an array of integers of size `numWindows+1` where the 0-th index represents the total number of customers served by the DMV and indexes `1` to `numWindows` represent the number of customers served at each window
<br>
## Clarifications and Assumptions
- There is only one queue. Not one per window.
- Customer arrival data is sortedby arrival timestamp
- Multiple customers can arrive at the same timestamp. They should be served in the order given in the input data
- If there are multiple available windows to serve a customer, the window with the lowest index must be chosen (Eg, If 2,5,7 are available, 2 must be chosen to serve the customer)
- Queue is first in first out. But the customer can drop out from the middle in case of timeout. In such cases, the next customer would move forward in the queue and one spot becomes available in the queue.
- If a customer arrives at a timestamp when the queue is full but a window becomes avaialble exactly at that time, you should not send the customer home. During a timestamp `tick`, move any eligible customers off the queue before attemping to add new arrivals.
- All the windows must be included in the output, even if some of them has not served any clients
- `numCustomers` is an integer within the range [0, 2^31 - 1]
- `numWindows` is an integer within the range [0, 2^31 -1]
- `customers` is a zero-indexed array of strings, sorted ascending by timestamp
- `queueSize` is an integer within the range [0, 2^31 -1]
- Each arrival time is an integer in the range [0, 2^31 -1]. Overflows are possible when calculating future timestamps from the arrival timestamp.
- `serviceTime` and `toleranceTime` are integers in the range [1, 2^31 -1]
<br>
### Hints/ Things to consider
- Work incrementally! Get the simpler example cases working perfectly first, then tackle the more complex ones
- For scoring, it is more important to have the basic funcitonality working than to try to get it all at once.
For example, a submission that "just needs a few more lines of code" but doesn't work for _any_ example text case will likely receive a lower score than a submission that works for at least one of the example test cases.
<br>
## Example
For example, given `numWindows` = 2, `queueSize` = 1, and the following customer arrival data:
``` ["0,25,600", "5,20,600", "10,20,8", "15,50,100", "20,100,20"] ```
your functions should return:
```[3,2,1]```
where:
3 = customers successfully served out of 5 customers visiting the DMV
2 = customers served at Window 1
1 = customer served at Window 2
## Explanation
`Wx` represents Window `x` where `x=1` to `numWindows(2)`
`Cy` represents Customer `y` where `y=1` to `numCustomers(5)`
"""



