class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return False


if __name__ == '__main__':
    sol = Solution()
    assert sol.checkInclusion('ab', 'eidbaooo') is True
    assert sol.checkInclusion('ab', 'eidboaoo') is False
