from collections import Counter, defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = list()
        word_freq = Counter(words)
        word_len = len(words[0])

        for i in range(word_len):
            start = i
            m = 0
            tmp_dict = defaultdict(int)

            for j in range(i, len(s) + 1, word_len):
                if m == len(words):
                    res.append(start)

                word = s[j:j + word_len]

                if word not in word_freq:
                    start = j + word_len
                    m = 0
                    tmp_dict = defaultdict(int)
                    continue

                tmp_dict[word] += 1
                m += 1

                while tmp_dict[word] > word_freq[word]:
                    tmp_dict[s[start:start + word_len]] -= 1
                    start += word_len
                    m -= 1

        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
    assert sol.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]) == [6,9,12]
