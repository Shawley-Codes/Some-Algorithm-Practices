#Scott Hawley

class Stack:
    #constructor
    def _init_(self):
        self.items = []
    #check if empty stack
    def is_empty(self):
        return self.items ==[]
    #push an item into the last position
    def push(self, data):
        self.items.append(data)
    #remove the item at the last position
    def pop(self):
        return self.items.pop()


"""
Driver Code
"""

s = Stack()

s.push(1)
s.push(2)
s.push(3)
print(s.pop())
