class Solution:
    def generateParenthesis(self, n: int) -> list:
        def helper(st='', left=0, right=0):
            temp = list()
            if len(st) == 2*n:
                return [st]
            if left < n:
                temp += helper(st+'(', left+1, right)
            if left > right:
                temp += helper(st+')', left, right+1)
            return temp

        res = helper()
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.generateParenthesis(1) == ["()"]
    assert sol.generateParenthesis(2) == ["(())", "()()"]
    assert sol.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sol.generateParenthesis(4) == ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())',
                                          '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()',
                                          '()()(())', '()()()()']
