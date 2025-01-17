def maxProfitBruteForce(arr):
    max_profit = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                max_profit = max(arr[j] - arr[i], max_profit)
    return max_profit

def maxProfitOptimal(arr):
    min_price = float('inf')
    max_profit = 0
    for price in arr:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
