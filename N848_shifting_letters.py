class Solution:
    def shiftingLetters(self, s: str, shifts: list) -> str:
        alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
        shift_sum = sum(shifts)
        res = ''

        def get_shift(letter, shift):
            cur_ord = alphabet.index(letter)
            new_ord = (cur_ord + shift % len(alphabet)) % len(alphabet)
            return alphabet[new_ord]

        for i, v in enumerate(s):
            res += get_shift(v, shift_sum)
            shift_sum -= shifts[i]

        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.shiftingLetters('abc', [3, 5, 9]) == 'rpl'
    assert sol.shiftingLetters('aaa', [1, 2, 3]) == 'gfd'
    assert sol.shiftingLetters('abcd', [3, 5, 9, 11]) == 'cawo'
    assert sol.shiftingLetters('abcde', [3, 5, 9, 11, 100]) == 'ywska'
