from typing import *
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        s_len = len(s)

        p_hash = Counter(p)
        s_hash = Counter(s[:p_len])

        res = []
        for i in range(0, s_len-p_len+1):
            if len(s_hash - p_hash) == 0:
                res.append(i)
            if i < s_len-p_len:
                s_hash[s[i+p_len]] += 1
                s_hash[s[i]] -= 1

        return res


if __name__ == '__main__':
    print(ord('a'))
    sol = Solution()
    assert sol.findAnagrams('a', 'b') == []
    assert sol.findAnagrams('a', 'a') == [0]
    assert sol.findAnagrams('ab', 'abc') == []
    assert sol.findAnagrams('abc', 'abc') == [0]
    assert sol.findAnagrams('cba', 'abc') == [0]
    assert sol.findAnagrams('cbaebabacd', 'abc') == [0, 6]
    assert sol.findAnagrams('abab', 'ab') == [0, 1, 2]
    assert sol.findAnagrams('ababababab', 'ab') == [0, 1, 2, 3, 4, 5, 6, 7, 8]
