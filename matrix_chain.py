# matrix chain multiplication </3

# PUT d_i HERE
dimensions = [1,5,2,6,1,4]
# all first dimensions and last two dimensions

n = len(dimensions)
M = [[('','') for x in range(n)] for x in range(n)]
# cells of M are (min #, k = splitting point)
# - essentially holds the M matrix and the S matrix
# matrix chain multiplications

def FillM(p, M):
    # diagonal is 0
    for i in range(n):
        M[i][i] = (0,0)
    
    for L in range(2,n):
        for i in range(1,n-L+1):
            j=i+L-1
            M[i][j] = (1e7,-9)    # max integer
            for k in range(i,j):
                q = M[i][k][0] + M[k+1][j][0] + p[i-1]*p[k]*p[j]
                if q < M[i][j][0]:
                    M[i][j] = (q, k)
    #return M[1][n-1]

def printM(M):
    rowCount = len(M)
    colCount = len(M[0])
    
    # header for columns
    string = "i\j "
    for i in range(1,rowCount):
        string += f"{i}       "
    print(string)
    
    # print rows
    for rowIn, row in enumerate(M):
        if rowIn == 0: continue
        string = f"{rowIn} "
        for colIn, col in enumerate(row):
            if colIn == 0: continue
            string += f"{M[rowIn][colIn]} "
        print(string)

def printorder(M, i, j):
    if i==j:
        print(f"A{i}",end='')
    else:
        print('(',end='')
        printorder(M, i, M[i][j][1])
        print(')x(',end='')
        printorder(M, M[i][j][1]+1,j)
        print(')',end='')

FillM(dimensions, M)
printM(M)
printorder(M,1,n-1)