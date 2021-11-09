class Solution:
    def partition(self, s: str) -> list:
        res, queue = [], [([], s)]
        while queue:
            r, st = queue.pop(0)
            if len(st) == 0:
                res.append(r)
            else:
                for i in range(1, len(st)+1):
                    if st[:i] == st[i-1::-1]:
                        queue.append((r + [st[:i]], st[i:]))
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.partition('a') == [['a']]
    assert sol.partition('ab') == [['a', 'b']]
    assert sol.partition('aba') == [['aba'], ['a', 'b', 'a']]
    assert sol.partition('aab') == [['aa', 'b'], ['a', 'a', 'b']]
    assert sol.partition('aab') == [['aa', 'b'], ['a', 'a', 'b']]
    assert sol.partition('aabaa') == [['aabaa'], ['a', 'aba', 'a'], ['aa', 'b', 'aa'], ['a', 'a', 'b', 'aa'],
                                      ['aa', 'b', 'a', 'a'], ['a', 'a', 'b', 'a', 'a']]
