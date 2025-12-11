# Dat1_BestTimeBuySell.py
# ProblemsL Best Time to Buyy and Sell Stocks
# Concept: Track min price and max profit
# Notes: One Pass Advantage 

def maxProfit(prices):
    if not prices:
        return 0
    minPrice=float('inf')
    maxProfit=0
    for price in prices:
        minPrice=min(price,minPrice)
        maxProfit=max(0,maxProfit)
    return maxProfit

if __name__ == "__main__":
     
     print(maxProfit([7,1,5,3,6,4]))  # Expected: 5
     print(maxProfit([7,6,4,3,1]))    # Expected: 0
     print(maxProfit([1,2,3,4,5]))    # Expected: 4 