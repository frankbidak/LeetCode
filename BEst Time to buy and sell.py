prices = [7,1,5,3,6,4]

minPrice = float('inf')
maxProfit = 0

n = len(prices)

for i in range(n):
    minPrice = min(prices[i],minPrice)
    maxProfit = max (prices[i] - minPrice,maxProfit)
    
print(maxProfit)
