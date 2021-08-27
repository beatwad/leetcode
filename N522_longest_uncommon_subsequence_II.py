class Solution:
    def findLUSlength(self, strs: list) -> int:
        max_len = 0

        nums_dict = {i: len(v) for i, v in enumerate(strs)}
        sorted_nums = [strs[k] for k, v in sorted(nums_dict.items(), key=lambda kv: kv[1], reverse=True)]

        if len(sorted_nums[-1]) > len(sorted_nums[-2]):
            return len(sorted_nums[-1])

        for i, st1 in enumerate(sorted_nums):
            for st2 in sorted_nums[i+1:]:
                if st1 in st2:
                    break
            else:


        if max_len == 0:
            return -1
        return max_len


if __name__ == '__main__':
    sol = Solution()
    assert sol.findLUSlength(["aabbcc", "aabbcc", "cb", "abc"]) == 3
    assert sol.findLUSlength(['aa', 'aa', 'bcdef']) == 5
    assert sol.findLUSlength(['bc', 'cd', 'bcdef']) == 5
    assert sol.findLUSlength(['aabbcc', 'aabbcc', 'cb']) == 2
    assert sol.findLUSlength(['aba', 'cdc', 'eae']) == 3
    assert sol.findLUSlength(['aaa', 'aaa', 'aa']) == -1
    assert sol.findLUSlength(['aaa', 'aaa', 'a']) == -1
    assert sol.findLUSlength(['aaa', 'aa', 'a']) == 3
