n,k = 4,2
nums = list(range(1, k + 1)) + [n + 1]

print(nums)

output = []
j = 0

while j < k:
    # add current combination
    output.append(nums[:k])
    j = 0
    
    while j < k and nums[j + 1] == nums[j] + 1:
        nums[j] = j + 1
        j += 1
    nums[j] += 1
    
print(output)
