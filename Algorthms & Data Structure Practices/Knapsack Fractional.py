#Scott Hawley

"""
Knapsack Fractional
"""
#this class sotores data to make comparisons of cost
class ItemValue:
    def __init__(self,val,weight,index):
        self.val = val
        self.weight = weight
        self.index = index
        self.cost = val//weight #convert fraction to int value

    #special method name recognised by python to allow class division
    #this is used for sorting, to recognise which
    def __lt__(self, other):
        return self.cost < other.cost


def findMaxFractionalBenefit(val,weight,weightTotal):
    #create a matrix and fill it with classes for each weight
    matrix = []
    for i in range(len(weight)):
        matrix.append(ItemValue(val[i], weight[i], i))
        
    #sort the matrix, this increases time complexity significantly
    #sorts by cost using __1t__
    matrix.sort(reverse = True)

    total = 0
    for j in matrix:
        currentWeight = int(j.weight)
        currentVal = int(j.val)
        if weightTotal - currentWeight >= 0:
            weightTotal -= currentWeight
            total += currentVal
        #if you need to make a fraction you have run out of space and abort loop
        else:
            fraction = weightTotal / currentWeight #fraction is a float variable
            total += currentVal * fraction #get the value of taken from the fraction
            weightTotal = int(weightTotal - (currentWeight * fraction))
            break
    return total


"""
Driver Code
"""

val = [60,10,120,200]
weight = [10,20,30,40]
weightTotal = 50
knapsack = findMaxFractionalBenefit(val,weight,weightTotal)
print("Max value in fractional knapsack:", knapsack)
