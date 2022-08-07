def sumArray(n):
    total = 0
    for i in n:
        total+=i
    return total
    
    
nums = [-2,-1]
n = len(nums)
largest = -100
subArray = []

for i in range(n):
    for j in range(i,n):
        print(largest)
        if sumArray(nums[i:j+1]) > largest:
            largest = sumArray(nums[i:j+1])
            subArray = nums[i:j+1]

