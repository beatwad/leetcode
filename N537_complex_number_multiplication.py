class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        c1 = num1.split('+')
        c1[0], c1[1] = int(c1[0]), int(c1[1].rstrip('i'))
        c2 = num2.split('+')
        c2[0], c2[1] = int(c2[0]), int(c2[1].rstrip('i'))
        real = c1[0]*c2[0] - c1[1]*c2[1]
        img = c1[0]*c2[1] + c1[1]*c2[0]
        res = str(real) + '+' + str(img) + 'i'
        return res


if __name__ == '__main__':
    sol = Solution()
    assert (sol.complexNumberMultiply('0+0i', '0+0i') == '0+0i')
    assert (sol.complexNumberMultiply('0+-0i', '0+0i') == '0+0i')
    assert (sol.complexNumberMultiply('0+1i', '0+1i') == '-1+0i')
    assert (sol.complexNumberMultiply('1+1i', '1+1i') == '0+2i')
    assert (sol.complexNumberMultiply('1+-1i', '1+-1i') == '0+-2i')
    assert (sol.complexNumberMultiply('1+-0i', '1+0i') == '1+0i')
    assert (sol.complexNumberMultiply('1+-1i', '1+1i') == '2+0i')
    assert (sol.complexNumberMultiply('-1+1i', '-1+1i') == '0+-2i')
    assert (sol.complexNumberMultiply('-1+-1i', '-1+1i') == '2+0i')
    assert (sol.complexNumberMultiply('3+7i', '2+10i') == '-64+44i')
    assert (sol.complexNumberMultiply('-3+7i', '2+10i') == '-76+-16i')
    assert (sol.complexNumberMultiply('3+-7i', '2+10i') == '76+16i')
    assert (sol.complexNumberMultiply('-3+-7i', '2+10i') == '64+-44i')
