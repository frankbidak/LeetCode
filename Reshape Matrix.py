mat = [[1,2],[3,4]]
temp = []
r=4
c=1

temp = [j for i in mat for j in i ]
print(temp)

if r * c == len(temp):
    print([temp[i*c:(i + 1)*c] for i in range(r)])
else:
    print(nums)

