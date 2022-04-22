from typing import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_list = ['+', '-', '*', '/']

        def get_op(a, b, op):
            a, b = int(a), int(b)
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
            return int(a / b)

        stack = list()
        while len(tokens) > 0:
            token = tokens.pop(0)
            if token in op_list:
                b = stack.pop()
                a = stack.pop()
                stack.append(get_op(a, b, token))
            else:
                stack.append(token)

        return int(stack[0])


if __name__ == '__main__':
    sol = Solution()
    # 2
    assert sol.evalRPN(["2"]) == 2
    # 20 / 10
    assert sol.evalRPN(["20", "10", "/"]) == 2
    # 20 / -10
    assert sol.evalRPN(["20", "-10", "/"]) == -2
    # ((2 + 1) * 3)
    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9
    # (4 + (13 / 5))
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
    # ((10 * (6 / ((9 + 3) * -11))) + 17)
    assert sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
