height = [1,8,1,1,1,1,1,1,1]
maxArea = 0

lo = 0
hi = len(height)-1

for i in range(len(height)):
    for j in range(i+1,len(height)):
        h = min(height[i],height[j])
        w = j - i
    
        maxArea = max(maxArea,h*w)

print(maxArea)
