class Solution:
    def frequencySort(self, s: str) -> str:
        freq_dict = dict()
        res = ''
        for c in s:
            if c not in freq_dict:
                freq_dict[c] = 1
            else:
                freq_dict[c] += 1
        freq_dict = [(k, v) for k, v in sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)]
        for k, v in freq_dict:
            res += k*v
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.frequencySort('tree') == 'eetr'
    assert sol.frequencySort('cccaaa') == 'cccaaa'
    assert sol.frequencySort('a') == 'a'
    assert sol.frequencySort('aa') == 'aa'
    assert sol.frequencySort('aAbb') == 'bbaA'
    assert sol.frequencySort('bbaaaA') == 'aaabbA'
