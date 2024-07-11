def maxProfit(prices):
    # solution tracking min value, my first though
    min_value = prices[0]
    current_profit = 0
    for i in range(1, len(prices)):
        current_price = prices[i]
        if current_price > min_value:
            if current_price - min_value > current_profit:
                current_profit = current_price - min_value
        else:
            if current_price < min_value:
                min_value = current_price
    return current_profit


def maxProfit2(prices):
    # solution with 2 pointers
    l, r = 0, 1
    maxP = 0
    while r < len(prices):
        if prices[r] > prices[l]:
            maxP = max(prices[r] - prices[l], maxP)
        else:
            l = r
        r += 1
    return maxP


print(maxProfit([8, 3, 4, 6, 1, 2, 4]))
print(maxProfit2([8, 3, 4, 6, 1, 2, 4]))
