class Solution:
    def shiftingLetters(self, s: str, shifts: list) -> str:
        s = list(s)
        abc = 'abcdefghijklmnopqrstuvwxyz'
        abc_dict = dict()
        shift_sum = sum(shifts)

        for i in range(ord('a'), ord('z')+1):
            abc_dict[chr(i)] = i - ord('a')

        for i in range(len(s)):
            idx = (abc_dict[s[i]] + shift_sum) % len(abc)
            s[i] = abc[idx]
            shift_sum -= shifts[i]

        return ''.join(s)


if __name__ == '__main__':
    sol = Solution()
    assert sol.shiftingLetters('a', [300]) == 'o'
    assert sol.shiftingLetters('abc', [3, 5, 9]) == 'rpl'
    assert sol.shiftingLetters('aaa', [1, 2, 3]) == 'gfd'
    assert sol.shiftingLetters('abcd', [3, 5, 9, 11]) == 'cawo'
    assert sol.shiftingLetters('abcde', [3, 5, 9, 11, 100]) == 'ywska'
