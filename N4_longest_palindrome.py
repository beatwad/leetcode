class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        n = len(s)
        lp = s[0]
        i = 0
        while i < n:
            l = r = i
            # find substring with the same symbols
            while r+1 < n:
                if s[r+1] == s[i]:
                    r += 1
                else:
                    break
            i += r - i + 1
            # try to expand substring by finding the same symbols on it's begin and end
            while l-1 >= 0 and r+1 < n:
                if s[l-1] == s[r+1]:
                    l -= 1
                    r += 1
                else:
                    break
            if len(s[l:r+1]) > len(lp):
                lp = s[l:r+1]
        return lp


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome("bb") == "bb"
    assert sol.longestPalindrome("ac") == "a"
    assert sol.longestPalindrome("abc") == "a"
    assert sol.longestPalindrome("abab") == "aba"
    assert sol.longestPalindrome("ababa") == "ababa"
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("abbaa") == "abba"
    assert sol.longestPalindrome("abbbaa") == "abbba"

