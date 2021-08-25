class Solution:
    def intToRoman(self, num: int) -> str:
        th_dict = {0: '', 1: 'M', 2: 'MM', 3: 'MMM'}
        hund_dict = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
        ten_dict = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
        one_dict = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}

        main_dict = {0: one_dict, 1: ten_dict, 2: hund_dict, 3: th_dict}
        res = ''

        for i in range(3, -1, -1):
            nom = divmod(num, 10**i)
            nom, num = nom[0], nom[1]
            res += main_dict[i][nom]

        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.intToRoman(1) == 'I'
    assert sol.intToRoman(3) == 'III'
    assert sol.intToRoman(4) == 'IV'
    assert sol.intToRoman(9) == 'IX'
    assert sol.intToRoman(10) == 'X'
    assert sol.intToRoman(58) == 'LVIII'
    assert sol.intToRoman(1994) == 'MCMXCIV'
    assert sol.intToRoman(3999) == 'MMMCMXCIX'

