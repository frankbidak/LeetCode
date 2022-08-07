def backtrack(f):
    if f == n:
        output.append(nums[:])
        print(output)
    for i in range(f,n):
        nums[f] , nums[i] = nums[i] , nums[f]
        backtrack(f + 1)
        nums[f] , nums[i] = nums[i] , nums[f]

nums = [1,2,3]
n = len(nums)
output = []
backtrack(0)
print(output)
