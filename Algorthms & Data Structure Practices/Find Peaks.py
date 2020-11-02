#Scott Hawley

import time
import random

"""Array Time Tests"""
def sortingForPeak(A):
    """
    Time: n
    Space: constant
    """
    sort(A)
    return A[-1]

def findPeakSol2(A, low, high, size):
    """
    Time: log(n)
    Space: constant

    This algorithm attempts to find a peak
    starting from the middle element
    It recursivly calls and changes the middle
    by narrowing its low and high search ranges
    """
    #ex:  6   + (10  - 6) /2 = 8 
    mid = low + (high-low)/2
    mid = int(mid)
    #return middle element if it is a peak 
    if ((mid == 0 or A[mid - 1] <= A[mid]) and
        (mid == n - 1 or A[mid + 1] <= A[mid])):
        return mid
    
    elif (mid > 0 and A[mid - 1] > A[mid]):
        #move left
        findPeakSol2(A,low,(mid-1),n)
    else:
        #move right
        findPeakSol2 (A, (mid+1), high, n)

def findPeakSol3(A):
    """
    Time: n
    Space: constant

    This algorithm attempts to find a peak
    starting from the first element

    Devlog: Current issues stem from small arrays
    sometimes returning non instead of a proper peak
    [3,5,7,7] returns none when it should return 7
    """
    elem1 = A[0]
    elem2 = A[1]
    #ensure list is in range
    try:
        elem3 = A[2]
    except IndexError:
        elem3 = 0
    if elem1 >= elem2:
        return elem1
    elif elem2 >= elem1:
        if elem2 >= elem3:
            return elem2
        else:
            del A[0]
            #try:
            del A[1]
            #except IndexError: 
            findPeakSol3(A)
    else:
        return elem1;

def fillA(A):
    random.seed(time.time())
    for i in range(100000000):
        print("working: ", i) 
        A.append(random.randint(1,100))
    return A
    
"""
Driver Code
"""
A = []
A = fillA(A)
start_time = time.time()
peak = sortingForPeak(A)
#Peak = findPeakSol3(A)
#Peak = findPeakSol2(A,0,n-1,n)
elapsed_time = time.time() - start_time
print(elapsed_time)
print(peak)
#print(A[Peak])
#print(A[Peak])
