#Scott Hawley


"""
Fibonacci numbers with space complexity O(1)
"""
def computeFibonacci(n):
    if n<0:
        pass
    #first and second numbers in sequence is always 0 and 1, no value below
    elif n==0:
        return 0
    elif n==1:
        return 1
    #two recursive calls that go down to 0 or 1
    else:
        return computeFibonacci(n-1)+computeFibonacci(n-2)

"""
Driver Code
"""
fib = computeFibonacci(13)
print("Value 13 in a Fibonacci sequence: ",fib)
