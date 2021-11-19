class Solution(object):
    def diffWaysToCompute(self, input: str):
        input_dict = dict()
        return self.helper(input, input_dict)

    def helper(self, input, input_dict):
        if input in input_dict:
            return input_dict[input]
        if input.isdigit():
            input_dict[input] = int(input)
            return [int(input)]
        r = list()
        for i, c in enumerate(input):
            if c in "*-+":
                a = self.diffWaysToCompute(input[:i])
                b = self.diffWaysToCompute(input[i+1:])
                k = [eval(str(x) + c + str(y)) for x in a for y in b]
                r.extend(k)
                input_dict[input] = k
        return r


if __name__ == '__main__':
    sol = Solution()
    assert sol.diffWaysToCompute("2-1-1") == [2, 0]
    assert sol.diffWaysToCompute("2*3-4*5") == [-34, -10, -14, -10, 10]
    assert sol.diffWaysToCompute("2*1-1+5*3-2") == [-10, -26, -10, -26, -30, 10, 26, -10, 10, -34, -38, 26, -34, 26,
                                                    -4, -12, -4, -12, -14, 5, 13, 6, 14, -10, 10, -4, 5, 6, -32, -36,
                                                    28, -32, 28, -16, -18, 13, 14, -32, 28, -14, 13, 16]
