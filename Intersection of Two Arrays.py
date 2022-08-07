from collections import defaultdict
nums1 = [9,4,9,8,4,3,4,5]
nums2 = [4,9,5,8]

counter = collections.Counter(nums1)
ans = []

for num in nums2:
    if counter[num]>0:
        counter[num]-=1
        ans.append(num)
        
print(ans)
        
