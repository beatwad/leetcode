class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            match = i < len(s) and (s[i] == p[j] or p[j] == '?' or p[j] == '*')

            if p[j] == '*':
                ans = (match and dp(i+1, j) or dp(i, j+1) or (match and dp(i+1, j+1)))
            else:
                ans = match and dp(i+1, j+1)

            memo[(i, j)] = ans

            return ans

        return dp(0, 0)


if __name__ == '__main__':
    sol = Solution()
    assert sol.isMatch('', '') is True
    assert sol.isMatch('', 'a') is False
    assert sol.isMatch('a', '') is False
    assert sol.isMatch('a', 'a') is True
    assert sol.isMatch('aa', 'a') is False
    assert sol.isMatch('aa', '*') is True
    assert sol.isMatch('aa', '?a') is True
    assert sol.isMatch('ab', '?a') is False
    assert sol.isMatch('aa', 'a*a') is True
    assert sol.isMatch('aa', 'a*b') is False
    assert sol.isMatch('aa', 'a**a') is True
    assert sol.isMatch('aa', 'a***a') is True
    assert sol.isMatch('aa', '?***?') is True
    assert sol.isMatch('aa', '?***b') is False
    assert sol.isMatch('aa', '?*?*b') is False
    assert sol.isMatch('aa', '?*?*a') is False
    assert sol.isMatch('aa', '**?*a') is True
    assert sol.isMatch('a', '*a*') is True
    assert sol.isMatch('aa', '**a**a**') is True
    assert sol.isMatch('aba', 'a**?*a') is True
    assert sol.isMatch('aba', 'a*****?******a') is True
    assert sol.isMatch('abcde', 'abcd?') is True
    assert sol.isMatch('abcde', 'abcd*') is True
    assert sol.isMatch('abcde', 'abcd**********') is True
    assert sol.isMatch('abcde', 'abcd**********b') is False
    assert sol.isMatch('abcde', '****abcd**********b') is False


