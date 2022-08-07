l1 = [[0,6],[9,10],[13,23],[24,25],[34,35]]
l2 = [[1,5],[8,12],[15,24],[25,26]]
res = []

i = 0
j = 0

while i<len(l1) and j<len(l2):
    lo = max(l1[i][0],l2[j][0])
    hi = min(l1[i][1],l2[j][1])
    
    if lo<hi:
        res.append([lo,hi])
    
    if l1[i][1] < l2[j][1]:
        i+=1
    else:
        j+=1
        
    
print(res)