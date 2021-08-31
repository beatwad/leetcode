class Solution:
    def findLUSlength(self, strs: list) -> int:
        sorted_nums = sorted(strs, key=lambda x: -len(x))

        def is_subsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)

        for i, st1 in enumerate(sorted_nums):
            for st2 in sorted_nums[:i] + sorted_nums[i+1:]:
                if is_subsequence(st1, st2):
                    break
            else:
                return len(st1)
        return -1


if __name__ == '__main__':
    sol = Solution()
    assert sol.findLUSlength(["aabbcc", "aabbcc", "cb", "abc"]) == 2
    assert sol.findLUSlength(['aa', 'aa', 'bcdef']) == 5
    assert sol.findLUSlength(['bc', 'cd', 'bcdef']) == 5
    assert sol.findLUSlength(['aabbcc', 'aabbcc', 'cb']) == 2
    assert sol.findLUSlength(['aba', 'cdc', 'eae']) == 3
    assert sol.findLUSlength(['aaa', 'aaa', 'aa']) == -1
    assert sol.findLUSlength(['aaa', 'aaa', 'a']) == -1
    assert sol.findLUSlength(['aaa', 'aa', 'a']) == 3
