from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = list()

        def helper(a, tmp):
            if len(tmp) == k:
                res.append(tmp)
            else:
                for i in range(len(a)):
                    helper(a[i+1:], tmp + [a[i]])

        helper([i+1 for i in range(n)], [])
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.combine(1, 1) == [[1]]
    assert sol.combine(2, 1) == [[1], [2]]
    assert sol.combine(3, 2) == [[1, 2], [1, 3], [2, 3]]
    assert sol.combine(4, 3) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
    assert sol.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
