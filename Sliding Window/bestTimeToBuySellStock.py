# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0

    lowest = prices[0]
    max_profit = 0
    for price in prices:
        if price < lowest:
            lowest = price
        max_profit = max(max_profit, price-lowest)
    return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    max_profit = maxProfit(prices)
    assert max_profit == 5

    prices = [7, 6, 4, 3, 1]
    max_profit = maxProfit(prices)
    assert max_profit == 0

    prices = [2, 1, 4]
    max_profit = maxProfit(prices)
    assert max_profit == 3

    prices = []
    max_profit = maxProfit(prices)
    assert max_profit == 0
