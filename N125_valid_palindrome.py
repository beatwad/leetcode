import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return s == s[::-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.isPalindrome(' ') is True
    assert sol.isPalindrome('!') is True
    assert sol.isPalindrome('!!') is True
    assert sol.isPalindrome('ab') is False
    assert sol.isPalindrome('aa') is True
    assert sol.isPalindrome('a!a') is True
    assert sol.isPalindrome('A man, a plan, a canal: Panama') is True
    assert sol.isPalindrome('race a car') is False
    assert sol.isPalindrome('race e car') is True
