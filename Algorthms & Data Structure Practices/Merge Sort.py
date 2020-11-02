#Scott Hawley

def mergeSort(arr):
    """
    Recursivly sort an array by spliting it in half and sorting each half
    """
    if len(arr) > 1:
        #get values for merging by finding mid and then slicing array in half
        mid = len(arr)//2 #floor divinsion
        L = arr[:mid] #everything before mid
        R = arr[mid:] #everything after mid

        mergeSort(L) #recursively call first half
        mergeSort(R) #recursively call second half

        i = j = k = 0 #create variables set to zero for sorting

        #Copy data to arrays L & R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        #pass data back into array
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

"""
Driver Code
"""
def printArr(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

arr = [35,21,25,2,5,3,55]
printArr(arr)
mergeSort(arr)
printArr(arr)
