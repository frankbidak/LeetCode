triangle = [[-1],[2,3],[1,-1,-3]]
n = len(triangle)
total = triangle[0][0]

j = 0

for i in range(1,n):
    for j in range(i + 1):
        minAbove = 20000
        if j > 0:
            minAbove = triangle[i-1][j-1]
        if j < 0:
            minAbove = min(minAbove,triangle[i-1][j])
        
        triangle[i][j] += minAbove

for i in triangle: print(i)

print(min(triangle[-1]))
