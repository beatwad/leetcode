class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = prev = 0
        for i in range(len(s)):
            cur = roman_dict[s[i]]
            res += cur
            if prev > 0:
                if prev < cur:
                    res -= 2*prev
            prev = cur
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.romanToInt('III') == 3
    assert sol.romanToInt('IV') == 4
    assert sol.romanToInt('IX') == 9
    assert sol.romanToInt('LVIII') == 58
    assert sol.romanToInt('MCMXCIV') == 1994
    assert sol.romanToInt('MMMCMXCVIII') == 3998
    assert sol.romanToInt('MMMCMXCIX') == 3999
