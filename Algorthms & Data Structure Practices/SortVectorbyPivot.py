#Scott Hawley

import numpy as np

def rearrangeVector(vector, pivot):
    #set pivot to the start of array
    vector[pivot], vector[0] = vector[0], vector[pivot]
    i = 1
    k = vector.size
    for j in range(1, vector.size):
        #if the element is smaller than pivot shift it left
        if vector[j] < vector[pivot]:
            vector[i], vector[j] = vector[j], vector[i]
            i += 1
        #if the element is equal to pivot store temporarly at back
        if vector[j] == vector[pivot]:
            vector[k], vector[j] = vector[j], vector[k]
            k -= 1    
    vector[pivot], vector[i-1] = vector[i-1], vector[pivot]
    #this brings the script past O(n) in time,
    #but I could not think of another solution
    for h in range(k, vector.size):
        vector[h], vector[pivot+1] = vector[pivot+1], vector[h]

"""
Driver Code
"""
def printArr(vector):
    for i in range(vector.size):
        print(vector[i],end=" ")
    print()

vector = np.array([35,21,25,2,5,3,55])
pivot = vector.size//2
printArr(vector)
rearrangeVector(vector, pivot)
printArr(vector)
