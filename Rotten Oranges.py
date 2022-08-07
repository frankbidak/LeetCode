grid=[[2,0,1,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,1],[1,0,1,0,1,1,1,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,1,1,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]]
R, C = len(grid), len(grid[0])
rot = True
counter = 0

# Print Grid
for i in grid:
    print(i)

#--- Iterate grid
while rot:
    
    for i in range(R):
        for j in range(C):
            rot = False
            left = j - 1
            right = j + 1
            up = i - 1
            down = i + 1
            if grid[i][j] == 2:
                if left >= 0 and grid[i][left] == 1:
                    grid[i][left] = 2
                    rot = True
                if right < C and grid[i][right] == 1:
                    grid[i][right] = 2
                    rot = True
                if up >= 0 and grid[up][j] == 1:
                    grid[up][j] = 2
                    rot = True
                if down < R and grid[down][j] == 1:
                    grid[down][j] = 2
                    rot = True
    
                if rot:
                    counter = counter + 1

#--Print Grid
print("-------------------------------------------")
for i in grid:
    print(i)

#--Return Result
for orange in grid:
    if 1 in orange or counter == 0:
        print(-1)
    else:
        print(counter)
