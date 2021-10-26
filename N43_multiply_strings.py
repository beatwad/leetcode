class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        num3 = 0
        for i in range(n):
            radix = 0
            for j in range(m):
                mult = divmod((ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0')) + radix, 10)
                num3 += mult[1]*10**(i+j)
                radix = mult[0]
            num3 += radix*10**(i+m)
        return str(num3)


if __name__ == '__main__':
    sol = Solution()
    assert sol.multiply('0', '0') == '0'
    assert sol.multiply('0', '1') == '0'
    assert sol.multiply('1', '1') == '1'
    assert sol.multiply('5', '5') == '25'
    assert sol.multiply('7', '8') == '56'
    assert sol.multiply('11', '11') == '121'
    assert sol.multiply('14', '11') == '154'
    assert sol.multiply('14', '11') == '154'
    assert sol.multiply('67', '301') == '20167'
    assert sol.multiply('123', '456') == '56088'
    assert sol.multiply('639', '456') == '291384'
