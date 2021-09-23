class Sets:
    """ Class for initializing of set object """
    def __init__(self, x):
        self.value = x
        self.parent = self
        self.rank = 0


class SetOps:
    """ Class for operations with sets """
    def find_set(self, x):
        """ Find parent of set """
        if x != x.parent:
            x.parent = self.find_set(x.parent)
        return x.parent

    def link_sets(self, x, y):
        """ Links to sets with each other """
        if y.rank > x.rank:
            y.parent = x
        else:
            y.parent = x
            if x.rank == y.rank:
                x.rank += 1

    def union_sets(self, x, y):
        """ Find parents of both sets and link them to each other """
        self.link_sets(self.find_set(x), self.find_set(y))


if __name__ == '__main__':
    set1 = Sets(5)
    set2 = Sets(8)
    set3 = Sets(3)
    set4 = Sets(7)
    set5 = Sets(4)

    so = SetOps()
    so.union_sets(set1, set2)
    so.union_sets(set2, set3)
    so.union_sets(set4, set5)
    so.union_sets(set1, set5)

    assert set1.rank == 2
    assert set2.rank == 0
    assert set3.rank == 0
    assert set4.rank == 1
    assert set5.rank == 0

