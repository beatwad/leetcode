class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [''] * numRows
        incr = 1
        r = 0
        if numRows == 1:
            return s
        for v in s:
            res[r] += v
            r += incr
            if r < 0:
                r = 1
                incr = 1
            if r == numRows:
                r = numRows - 2
                incr = -1
        return ''.join(res)


if __name__ == '__main__':
    sol = Solution()

    assert sol.convert('A', 1) == 'A'
    assert sol.convert('PAYPAL', 2) == 'PYAAPL'
    assert sol.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert sol.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'