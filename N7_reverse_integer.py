class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        res = str(x)
        if res[0] == '-':
            sign = -1
            res = res[1:]
        res = res[::-1]
        if len(res) == 10:
            temp = res[:-1]
            if int(temp) > 214748364:
                return 0
            elif int(temp) == 214748364:
                if int(res[-1]) > 7 and sign == 1:
                    return 0
                if int(res[-1]) > 8 and sign == -1:
                    return 0
        return sign*int(res)


if __name__ == '__main__':
    sol = Solution()

    assert sol.reverse(123) == 321
    assert sol.reverse(-123) == -321
    assert sol.reverse(0) == 0
    assert sol.reverse(120) == 21
    assert sol.reverse(2**31-1) == 0
    assert sol.reverse(-2**31) == 0
    assert sol.reverse(7463847412) == 2**31-1
    assert sol.reverse(8463847412) == 0
    assert sol.reverse(-8463847412) == -2**31
    assert sol.reverse(-9463847412) == 0

    print(64 >> 1)

