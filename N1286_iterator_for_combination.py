class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.combs = list()
        self.len = combinationLength

        def backtracking(r, comb):
            if len(r) == self.len:
                self.combs.append(r)
            else:
                for i in range(len(comb)):
                    backtracking(r + [comb[i]], comb[i+1:])

        backtracking([], self.chars)

    def next(self) -> str:
        res = self.combs.pop(0)
        return ''.join(res)

    def hasNext(self) -> bool:
        if self.combs:
            return True
        return False


if __name__ == '__main__':
    sol = CombinationIterator('abcde', 3)
    assert sol.next() == 'abc'
    assert sol.next() == 'abd'
    assert sol.hasNext() is True
    assert sol.next() == 'abe'
    sol.next()
    sol.next()
    sol.next()
    sol.next()
    sol.next()
    assert sol.next() == 'bde'
    assert sol.next() == 'cde'
    assert sol.hasNext() is False
