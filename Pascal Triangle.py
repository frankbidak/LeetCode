numRows = 10
pt = [ [None for i in range(j)] for j in range(1,numRows+1)]

for i in range(numRows):
    pt[i][0] = 1
    pt[i][i] = 1

for i in range(2,numRows):
    for j in range(1,i):
        pt[i][j] = pt[i-1][j-1] + pt[i-1][j]

for i in pt:
    print(i)
