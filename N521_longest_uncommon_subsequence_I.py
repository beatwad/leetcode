class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))


if __name__ == '__main__':
    sol = Solution()
    assert sol.findLUSlength('a', 'b') == 1
    assert sol.findLUSlength('aba', 'cdc') == 3
    assert sol.findLUSlength('aaa', 'bbb') == 3
    assert sol.findLUSlength('aba', 'cba') == 3
    assert sol.findLUSlength('aaa', 'aaa') == -1
    assert sol.findLUSlength('aaaa', 'aaa') == 4
    assert sol.findLUSlength('aaa', 'aaaa') == 4
    assert sol.findLUSlength('aaa', 'bbbb') == 4