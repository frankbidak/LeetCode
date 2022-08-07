nums = [5,7,7,8,8,10]
result = []
target = 8


left = 0
right = len(nums) - 1

while nums[left] != target:
    left+=1

while nums[right] != target:
    right-=1


print(left,right)
