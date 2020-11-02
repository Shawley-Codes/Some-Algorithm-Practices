#Scott Hawley

"""
Interval Scheduling Problem (earliest finish time first)
"""
#function assumes the events are sorted according to finish time
def printMaxEventSchedule(start, finish):
    numEvents = len(finish)
    print("Events number",end = " ")

    #always choose the earliest event, i is the earliest considerable time
    i=0
    print (i+1,end = " ")

    for j in range(numEvents):
        if start[j] >= finish[i]:
            print (j+1,end = " ")
            #move earliest considerable time up
            i = j

"""
Driver Code
"""
#         1 2 3 4 5 6 7
start =  [0,0,2,2,4,4,5]
finish = [1,2,3,5,5,6,7]
printMaxEventSchedule(start,finish)
print("are selected!")

