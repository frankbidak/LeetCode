nums = [-1,0,-5,-3,1,2,-1,-4,4,1]
result=[]
nums.sort()
n = len(nums)
i = 0

while nums[i] <= 0:
    lo = i + 1
    hi = n - 1
    if nums[lo] + nums[hi] + nums[i] == 0:
        result.append([i,lo,hi])
    elif 0 - nums[lo] > nums[i] + nums[hi]:
        lo = lo + 1
    elif 0 - nums[hi] > nums[i] + nums[lo]:
        hi = hi - 1
    
    i+=1
    
print(result)
