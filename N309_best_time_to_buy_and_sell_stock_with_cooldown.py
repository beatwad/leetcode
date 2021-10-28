class Solution:
    def maxProfit(self, prices):
        # buy -> do nothing -> buy
        # buy -> sell stock -> cool
        # cool -> do nothing -> sell
        # sell -> do nothing -> sell
        # sell -> buy stock -> buy
        n = len(prices)
        buy = [0 for _ in range(n+1)]
        sell = [0 for _ in range(n+1)]
        # balance on first buy element should equal minus first price
        buy[1] = 0 - prices[0]
        for i in range(2, n+1):
            # you can stay in buy state if do nothing or sell stock and wait for 1 day (cooldown)
            buy[i] = max(buy[i-1], sell[i-2] - prices[i-1])
            # you can stay in sell state if do nothing or buy stock
            sell[i] = max(sell[i-1], buy[i-1] + prices[i-1])
        return max(buy[-1], sell[-1])


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProfit([1, 2, 3, 0, 2]) == 3
    assert sol.maxProfit([1]) == 0
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
