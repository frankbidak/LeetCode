def isPowerofTwo(n:int):
    if n == 0: return False
    
    if n % 2 == 0: isPowerofTwo(n/2)
    
    return n == 1

print(isPowerofTwo(1024))