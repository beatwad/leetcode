class Solution:
    def maxProfit(self, prices: list) -> int:
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[i-1]
            max_profit += max(profit, 0)

        return max_profit


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProfit([1, 5, 3, 7, 1, 5, 3, 6, 4]) == 15
    assert sol.maxProfit([5, 3, 7, 1, 5, 3, 6, 4]) == 11
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([1]) == 0
    assert sol.maxProfit([1, 2]) == 1
    assert sol.maxProfit([2, 1]) == 0
