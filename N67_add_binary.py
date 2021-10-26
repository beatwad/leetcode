class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        n, m = len(a), len(b)
        c = ''
        a, b, carry = list(a), list(b), 0
        for i in range(n):
            if i < m:
                res = divmod(int(a.pop()) + int(b.pop()) + carry, 2)
            elif carry == 0:
                c = ''.join(a) + c
                break
            else:
                res = divmod(int(a.pop()) + carry, 2)
            carry, res = res[0], str(res[1])
            c = res + c
        if carry:
            c = str(carry) + c
        return c


if __name__ == '__main__':
    sol = Solution()
    assert sol.addBinary('0', '0') == '0'
    assert sol.addBinary('1', '0') == '1'
    assert sol.addBinary('0', '1') == '1'
    assert sol.addBinary('1', '1') == '10'
    assert sol.addBinary('11', '1') == '100'
    assert sol.addBinary('111', '1') == '1000'
    assert sol.addBinary('1101', '1') == '1110'
    assert sol.addBinary('1110', '1') == '1111'
    assert sol.addBinary('10000', '1') == '10001'
