from A1_graph import Graph


class Solution:
    def extract_min(self, queue):
        """
        Extract minimal element from queue
        """
        min_el = min(queue, key=queue.get)
        del queue[min_el]
        return queue, min_el

    def mst_prim(self, gr, r_label):
        """
        Finds Minimal Spanning Tree (MST) for the Graph by Prim algorithm
        """
        r = gr.vertexes[r_label]
        r.dist = 0
        v_queue = {k: v.dist for k, v in gr.vertexes.items()}
        while v_queue:
            v_queue, u = self.extract_min(v_queue)
            for k, v in gr.vertexes[u].adj.items():
                if k in v_queue and gr.edges[(u, k)] < gr.vertexes[k].dist:
                    gr.vertexes[k].parent = gr.vertexes[u]
                    gr.vertexes[k].dist = gr.edges[(u, k)]
                    v_queue[k] = gr.edges[(u, k)]
        mst = [(gr.vertexes[k].parent.label, gr.vertexes[k].label) for k in gr.vertexes.keys() if k != r_label]
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

    assert sol.mst_prim(gr, 's') == [('s', 't'), ('s', 'x'), ('t', 'y'), ('y', 'z'), ('y', 'w'), ('z', 'n')]

    gr = Graph(['s', 't', 'x', 'y', 'z', 'w', 'n'])
    gr.add_edge('s', 't', 3, False)
    gr.add_edge('t', 'x', 2, False)
    gr.add_edge('t', 'y', 2, False)
    gr.add_edge('y', 'z', 4, False)
    gr.add_edge('y', 'w', 1, False)
    gr.add_edge('k', 'l', 8, False)
    gr.add_edge('l', 'o', 9, False)
    gr.add_edge('z', 'n', 3, False)
    gr.add_edge('x', 'z', 5, False)
    gr.add_edge('x', 's', 3, False)

    # s -3- t -2- y -1- w
    #  \    |     |
    #   3   2     4
    #    \  |     |
    #      x  -5- z -3- n

    assert sol.mst_prim(gr, 's') == [('s', 't'), ('t', 'x'), ('t', 'y'), ('y', 'z'), ('y', 'w'), ('z', 'n')]
