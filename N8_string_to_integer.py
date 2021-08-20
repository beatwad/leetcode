import re


class Solution:
    def myAtoi(self, s: str) -> int:
        res = ''.join([d for d in re.findall('^\s*[+-]?\d+', s)])
        if res == '':
            return 0
        res = int(res)
        res = min(res, 2**31-1)
        res = max(res, -2**31)
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.myAtoi("") == 0
    assert sol.myAtoi("  ") == 0
    assert sol.myAtoi("0") == 0
    assert sol.myAtoi("0a") == 0
    assert sol.myAtoi("   a") == 0
    assert sol.myAtoi("+-12") == 0
    assert sol.myAtoi("-+12") == 0
    assert sol.myAtoi("42") == 42
    assert sol.myAtoi("-42") == -42
    assert sol.myAtoi("-42.") == -42
    assert sol.myAtoi("   +42") == 42
    assert sol.myAtoi("   -42") == -42
    assert sol.myAtoi("   -4a2") == -4
    assert sol.myAtoi("   4A2") == 4
    assert sol.myAtoi("   42.2") == 42
    assert sol.myAtoi("4193 with words") == 4193
    assert sol.myAtoi("words and 987") == 0
    assert sol.myAtoi("   -12   a1234A") == -12
    assert sol.myAtoi("   -121234A") == -121234
    assert sol.myAtoi("2147483648") == 2147483647
    assert sol.myAtoi("91283472332") == 2147483647
    assert sol.myAtoi("-2147483648") == -2147483648
    assert sol.myAtoi("-91283472332") == -2147483648
