#Scott Hawley

"""
Longest Common Subsequence
"""
#X & Y are sequences input, x & y are the sequence length
def FindLCS(X,Y):
    x = len(X)
    y = len(Y)

    #fill a matrix with 0 the size of x & y
    matrix = [[0 for i in range(y+1)]for i in range(x+1)]
    for i in range(1, x+1):
        for j in range(1, y+1):
            #first value is always 0 on the first line of x & y
            if i == 0 or j == 0:
                matrix[i][j] = 0
            #if a value in the sequence matches...
            #add 1 to the location of the match
            elif X[i-1] == Y[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            #carry on the size of value to the right
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    index = matrix[x][y]
    lcs = [""]*index
    a = x
    b = y
    #start creating the subsequence
    while a > 0 and b > 0:
        if X[a-1] == Y[b-1]:
            lcs[index-1] = X[a-1]
            a -= 1
            b -= 1
            index -= 1

        elif matrix[a-1][b] > matrix[a][b-1]:
            a -= 1
        else:
            b -= 1
    return lcs

                                

"""
Driver Code
"""
X = "ABCDEFG"
Y = "BDFHJLP"
lcs = FindLCS(X,Y)
print("Longest Common Subsequence: ",lcs)
print("Sequence Length",len(lcs))
