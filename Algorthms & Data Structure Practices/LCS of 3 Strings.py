#Scott Hawley

"""
Longest Common Subsequence length of 3 strings
"""
#promoted to globals
X = "ABCDEFGH"
Y = "BDFHJLPR"
Z = "BDHJLPRS"
#make a massive matrix
matrix = [[[-1 for i in range(100)]
                 for j in range(100)]
                 for k in range(100)]

#recursion requires variables to come from outside as globabls
def FindLCS3(x,y,z):
    if(x == -1 or y == -1 or z == -1):
        return 0
    if(matrix[x][y][z] != -1):
        return matrix[x][y][z]
    if(X[x] == Y[y] and Y[y] == Z[z]):
        matrix[x][y][z] = 1 + FindLCS3(x-1,y-1,z-1)
        return matrix[x][y][z]
    else:
        matrix[x][y][z] = max(max(FindLCS3(x-1,y,z),FindLCS3(x,y-1,z)),FindLCS3(x,y,z-1))
        return matrix[x][y][z]

"""
Driver Code, gloabals above function
"""

x = len(X)
y = len(Y)
z = len(Z)
lcs = FindLCS3(x-1,y-1,z-1)
print("Length of subsequence: ", lcs)
