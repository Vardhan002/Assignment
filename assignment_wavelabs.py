from typing import List

def max_profit(prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0
    
    forward = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        forward[i] = max(forward[i-1], prices[i] - min_price)"subtracting the minimum price from the current price"
        
    
    backward = [0] * n
    max_price = prices[-1]
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        backward[i] = max(backward[i+1], max_price - prices[i])"subtracting the current price from the maximum price"
    
   
    total = 0
    for i in range(n):
        total = max(total,forward[i] + backward[i])    
    return total

def profit(prices: List[int]) -> int:
    return max_profit(prices)

if __name__ == '__main__':
    month1 = [3,3,5,0,0,3,1,4]
    print(profit(month1))

    month2 = [1,2,3,4,5] 
    print(profit(month2))

    month3 = [7,6,4,3,1]
    print(profit(month3))
