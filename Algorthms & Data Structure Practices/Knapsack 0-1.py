#Scott Hawley

"""
Knapsack 0-1
"""
def findMaxBenefit(val,weight,weightTotal,numVal):
    #create a matrix
    matrix = [[0 for x in range(weightTotal+1)]for x in range(numVal+1)]

    #fill in the matrix
    for i in range(numVal + 1):
        for j in range(weightTotal + 1):
            #fill in the first row and columb with 0
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif weight[i-1] <= j:
                matrix[i][j] = max(val[i-1] + matrix[i-1][j-weight[i-1]]
                                   , matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]

    return matrix[numVal][weightTotal]



"""
Driver Code
"""

val = [60,10,120]
weight = [10,20,30]
weightTotal = 50
numVal = len(val)
knapsack = findMaxBenefit(val,weight,weightTotal,numVal)
print("Max value in knapsack:", knapsack)
