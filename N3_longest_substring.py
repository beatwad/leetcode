class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) in [0, 1]:
            return len(s)
        l = 0
        r = l+1
        max_sub_len = 0
        while l < r < len(s):
            if s[r] in s[l:r]:
                dup_index = s[l:r].index(s[r])
                l += dup_index + 1
            if r - l + 1 > max_sub_len:
                max_sub_len = r - l + 1
            r += 1
        return max_sub_len


if __name__ == '__main__':
    sol = Solution()

    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring("a") == 1
    assert sol.lengthOfLongestSubstring("ab") == 2
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("abcd") == 4
