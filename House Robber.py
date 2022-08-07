nums = [1,2,3,1]
n = len(nums)

if not nums:
    print(0)

maxRobbed = [None] * (n+1)
print(maxRobbed)

# Base case initialization.
maxRobbed[n] = 0
maxRobbed[n - 1] = nums[n - 1]

print(maxRobbed)

# DP table calculations.
for i in range(n - 2, -1, -1):
    maxRobbed[i] = max(maxRobbed[i + 1], maxRobbed[i + 2] + nums[i])
    
    print(maxRobbed) 

