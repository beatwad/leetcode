class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i-1, -1, -1):
                if s[j:i] in wordDict and dp[j] is True:
                    dp[i] = True
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.wordBreak('leetcode', ['leet', 'code']) is True
    assert sol.wordBreak('applepenapple', ['apple', 'pen']) is True
    assert sol.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']) is False
