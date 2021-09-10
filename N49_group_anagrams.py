class Solution:
    def groupAnagrams(self, strs: list) -> list:
        anagrams_dict = dict()
        for st in strs:
            st_s = ''.join(sorted(st))
            if st_s not in anagrams_dict:
                anagrams_dict[st_s] = []
            anagrams_dict[st_s].append(st)
        return list(anagrams_dict.values())


if __name__ == '__main__':
    sol = Solution()
    assert sol.groupAnagrams(["bdddddddddd", "bbbbbbbbbbc"]) == [["bdddddddddd"], ["bbbbbbbbbbc"]]
    assert sol.groupAnagrams(["bzzz", "zzzc"]) == [["bzzz"], ["zzzc"]]
    assert sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'],
                                                                             ['bat']]
    assert sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat", ""]) == [['eat', 'tea', 'ate'], ['tan', 'nat'],
                                                                                 ['bat'], [""]]
    assert sol.groupAnagrams([""]) == [[""]]
    assert sol.groupAnagrams(["a"]) == [["a"]]


