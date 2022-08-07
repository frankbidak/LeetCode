grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

def maxArea(r,c):
    global counter
    global largest
    
    if grid[r][c] == 1:
        counter = counter + 1
        if r >= 1:
            maxArea(r-1, c)
        if r <= R:
            maxArea(r+1, c)
        if c >= 1:
            maxArea(r, c-1)
        if c <= C:
            maxArea(r, c+1)
        
        largest = max(counter,largest)

R,C = len(grid), len(grid[0])
counter = 0
largest = 0
i,j = 0,0


for i in range(len(grid)):
    for j in range(len(grid[0])):
        maxArea(i,j)

print(largest)
