class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            if p[j] == '*':
                res = (i < len(s) and dp(i+1, j)) or dp(i, j+1) or (i < len(s) and dp(i+1, j+1))
            elif i < len(s) and (s[i] == p[j] or p[j] == '?'):
                res = dp(i+1, j+1)
            else:
                res = False

            memo[(i, j)] = res

            return res

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


