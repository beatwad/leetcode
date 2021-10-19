class Solution:
    def maxProfit(self, prices: list) -> int:
        max_profit = 0
        buy = prices[0]

        if prices.index(max(prices)) > prices.index(min(prices)):
            return max(prices) - min(prices)

        for i in range(1, len(prices)):
            buy = min(prices[i], buy)
            max_profit = max(prices[i] - buy, max_profit)

        return max_profit


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([1, 1, 5, 3, 6, 8]) == 7
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
