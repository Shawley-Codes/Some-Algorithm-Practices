#Scott Hawley

class my_Queue:
    #constructor, sets capacity and initial array
    def __init__(self):
        self.items = []
        #self.capacity = capacity
    #checks if empty
    def isEmpty(self):
        return self.items == []
    #adds an item to the list, checks if there is capacity
    def enqueue(self, item):
        #if len(self.items) < self.capcity:
        self.items.insert(0,item)
    #removes the first item in the list
    def dequeue(self):
        return self.items.pop()
    #checks the current number of elements in the array
    def size(self):
        return len(self.items)

"""
Driver Code
"""

testQ = my_Queue()

testQ.enqueue(4)
testQ.enqueue('dog')
testQ.enqueue(1.2)
print(testQ.size())
print(testQ.dequeue())
