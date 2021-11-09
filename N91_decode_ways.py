class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, n+1):
            if int(s[i-1]) > 0:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.numDecodings('12') == 2
    assert sol.numDecodings('226') == 3
    assert sol.numDecodings('11106') == 2
    assert sol.numDecodings('11206') == 2
    assert sol.numDecodings('11306') == 0
    assert sol.numDecodings('0') == 0
    assert sol.numDecodings('06') == 0
    assert sol.numDecodings('80') == 0
    assert sol.numDecodings('802') == 0
    assert sol.numDecodings('8021') == 0

