from A1_graph import Graph
from A5_sets import Sets, SetOps


class Solution:
    def __init__(self):
        self.time = 0

    def mst_kruskal(self, gr):
        """
        Finds Minimal Spanning Tree (MST) for the Graph by Kruskal algorithm
        :param gr: Graph
        :return: list[tuple[int]] or list[tuple[str]]
        """
        mst = list()
        v_sets_dict = dict()
        so = SetOps()
        for u in gr.vertexes.values():
            v_sets_dict[u.label] = Sets(u.label)
        e_sorted = [k for k, v in sorted(gr.edges.items(), key=lambda x: x[1])]
        for e in e_sorted:
            u, v = v_sets_dict[e[0]], v_sets_dict[e[1]]
            if so.find_set(u) != so.find_set(v):
                mst.append(e)
                so.union_sets(u, v)
        return mst


if __name__ == '__main__':
    sol = Solution()

    gr = Graph(['s', 't', 'x', 'y', 'z', 'w', 'n'])
    gr.add_edge('s', 't', 3, False)
    gr.add_edge('t', 'x', 6, False)
    gr.add_edge('t', 'y', 2, False)
    gr.add_edge('y', 'z', 4, False)
    gr.add_edge('y', 'w', 1, False)
    gr.add_edge('k', 'l', 8, False)
    gr.add_edge('l', 'o', 9, False)
    gr.add_edge('z', 'n', 3, False)
    gr.add_edge('x', 'z', 5, False)
    gr.add_edge('x', 's', 1, False)

    # s -3- t -2- y -1- w
    #  \    |     |
    #   1   6     4
    #    \  |     |
    #      x  -5- z -3- n

    assert sol.mst_kruskal(gr) == [('y', 'w'), ('x', 's'), ('t', 'y'), ('s', 't'), ('z', 'n'), ('y', 'z')]
