class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        s_rev = s[::-1]
        if s == s_rev:
            return True
        return False


if __name__ == '__main__':
    sol = Solution()
    assert sol.isPalindrome(0) is True
    assert sol.isPalindrome(1) is True
    assert sol.isPalindrome(-1) is False
    assert sol.isPalindrome(121) is True
    assert sol.isPalindrome(-121) is False
    assert sol.isPalindrome(10) is False
    assert sol.isPalindrome(101) is True
    assert sol.isPalindrome(-101) is False
    assert sol.isPalindrome(1001) is True
    assert sol.isPalindrome(123321) is True
    assert sol.isPalindrome(343) is True
    assert sol.isPalindrome(3431) is False
    assert sol.isPalindrome(13431) is True
    assert sol.isPalindrome(11) is True
    assert sol.isPalindrome(121) is True
    assert sol.isPalindrome(1211) is False
