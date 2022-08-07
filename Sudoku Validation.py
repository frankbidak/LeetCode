s="loveleetcode"

for i in range(len(s)):
    if s[i] not in s[i+1:]:
        print(i)
        break
    else:
        print(-1)
        
