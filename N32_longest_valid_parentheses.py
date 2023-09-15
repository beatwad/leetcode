class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]

        for i, v in enumerate(s):
            if v == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestValidParentheses("((") == 0
    assert sol.longestValidParentheses(")(") == 0
    assert sol.longestValidParentheses(")()") == 2
    assert sol.longestValidParentheses("(()") == 2
    assert sol.longestValidParentheses("()(()") == 2
    assert sol.longestValidParentheses(")()())") == 4
    assert sol.longestValidParentheses(")(())(()))") == 8
