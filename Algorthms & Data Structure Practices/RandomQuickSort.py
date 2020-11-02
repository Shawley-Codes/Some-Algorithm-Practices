#Scott Hawley

import random

def randomQuickSort(arr, start, stop):
    """
    This function sorts by recursivly calling a random index
    and sorting around it. Start and Stop are indexes containing
    the beginings and ends of subarrays around a pivot.
    """
    if start < stop:
        #index where the pivot is lovated in array
        pivotIndex = randomizer(arr, start, stop)

        #recursively call sort to sort the left and right halves
        randomQuickSort(arr, start, pivotIndex-1)
        randomQuickSort(arr, pivotIndex+1,stop)

def randomizer(arr, start, stop):
    """
    Finds a random value in an array and passes it to a partitioner
    """
    randPivot = random.randrange(start, stop)

    #swap values start and pivot
    arr[start], arr[randPivot] = arr[randPivot], arr[start]
    return partition(arr, start, stop)

def partition(arr, start, stop):
    """
    This function takes the first value as pivot(we swapped rand pivot to first)
    and then re-arranges values according to the pivot.
    Smaller values to left of pivot and bigger values to right.
    """
    pivot = start #pivot is set to first value
    i = start+1 #array starts after pivot
    for j in range(start+1,stop+1):
        #if the element is smaller or equal to pivot then shift it left of pivot
        #which is the first value
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[pivot], arr[i-1] = arr[i-1], arr[pivot]
    pivot = i-1
    return(pivot)

"""
Driver Code
"""
def printArr(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

arr = [35,21,25,2,5,3,55]
printArr(arr)
randomQuickSort(arr, 0 , len(arr)-1)
printArr(arr)
