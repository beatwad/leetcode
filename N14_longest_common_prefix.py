class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ''
        if len(strs) == 0:
            return prefix
        for i in range(len(min(strs))):
            c = strs[0][i]
            if not all(a[i] == c for a in strs):
                return prefix
            else:
                prefix += c
        return prefix


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestCommonPrefix([]) == ''
    assert sol.longestCommonPrefix(['reflower', 'flow', 'flight']) == ''
    assert sol.longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
    assert sol.longestCommonPrefix(['flower', 'fl', 'flight']) == 'fl'
    assert sol.longestCommonPrefix(['dog', 'flow', 'rocket']) == ''