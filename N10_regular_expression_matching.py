class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if "*" not in p and '.' not in p:
            return s == p

        memo = dict()

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j+1 < len(p) and p[j+1] == '*':
                ans = dp(i, j+2) or (match and dp(i+1, j))
            else:
                ans = match and dp(i+1, j+1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)


if __name__ == '__main__':
    sol = Solution()
    assert sol.isMatch('a', 'a') is True
    assert sol.isMatch('a', 'b') is False
    assert sol.isMatch('aa', 'a.') is True
    assert sol.isMatch('aa', 'aa.') is False
    assert sol.isMatch('aaa', 'aaa.') is False
    assert sol.isMatch('abc', '.bc') is True
    assert sol.isMatch('abc', 'ab.') is True
    assert sol.isMatch('aa', 'aa') is True
    assert sol.isMatch('aa', 'a') is False
    assert sol.isMatch('aa', 'a*') is True
    assert sol.isMatch('ab', '.*') is True
    assert sol.isMatch('abc', '.*') is True
    assert sol.isMatch('abc', '....') is False
    assert sol.isMatch('abc', '..*') is True
    assert sol.isMatch('abc', '...*') is True
    assert sol.isMatch('abcd', 'abc*d') is True
    assert sol.isMatch('abcd', 'abc*.') is True
    assert sol.isMatch('abc', 'abc*.') is True
    assert sol.isMatch('abc', 'ab*.') is True
    assert sol.isMatch('abc', 'ab.*') is True
    assert sol.isMatch('abc', 'abc*') is True
    assert sol.isMatch('abc', 'ab*c') is True
    assert sol.isMatch('aaa', 'aa*a') is True
    assert sol.isMatch('aaaaa', 'aa*aaa') is True
    assert sol.isMatch('aaaaa', 'aa*a*a') is True
    assert sol.isMatch('abb', 'ab*b') is True
    assert sol.isMatch('abcd', 'ab*cd') is True
    assert sol.isMatch('aaaaaaaaaaaaaaaaaaa', 'a*a*a*a*a*a*a*a*a*a*') is True
    assert sol.isMatch('aaaaaaaaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*') is False
