class Solution:
    def threeSum(self, nums: list) -> list:
        ans = set([])
        plus = sorted([n for n in nums if n > 0])
        plus_c = set(plus)
        zero = [n for n in nums if n == 0]
        minus = sorted([n for n in nums if n < 0])
        minus_c = set(minus)
        # all zero
        if len(zero) > 2:
            ans.add((0, 0, 0))
        # plus zero minus
        if len(zero) > 0:
            for n in minus:
                if -n in plus_c:
                    ans.add((n, 0, -n))
        # plus minus minus
        n = len(minus)
        for i in range(n):
            for j in range(i+1, n):
                diff = -(minus[i]+minus[j])
                if diff in plus_c:
                    ans.add((minus[i], minus[j], diff))
        # plus plus minus
        n = len(plus)
        for i in range(n):
            for j in range(i+1, n):
                diff = -(plus[i]+plus[j])
                if diff in minus_c:
                    ans.add((diff, plus[i], plus[j]))
        return list(ans)


if __name__ == '__main__':
    sol = Solution()
    assert sol.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]) == [(-4, 1, 3),
                                                                               (-4, -2, 6),
                                                                               (-4, 2, 2),
                                                                               (-2, -2, 4),
                                                                               (-4, 0, 4),
                                                                               (-2, 0, 2)]
    assert sol.threeSum([-2, 0, 1, 1, 2]) == [(-2, 0, 2), (-2, 1, 1)]
    assert sol.threeSum([-1, -1, 0, 1, 1, 2]) == [(-1, 0, 1), (-1, -1, 2)]
    assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [(-1, 0, 1), (-1, -1, 2)]
    assert sol.threeSum([]) == []
    assert sol.threeSum([0]) == []
    assert sol.threeSum([0, 1]) == []
    assert sol.threeSum([0, 0, 0, 0]) == [(0, 0, 0)]
