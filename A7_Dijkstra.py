from A1_graph import Graph


class Solution:
    def extract_min(self, queue):
        """
        Extract minimal element from queue
        """
        min_el = min(queue, key=queue.get)
        del queue[min_el]
        return queue, min_el

    def relax(self, u, v, v_queue):
        """
        Extract minimal element from queue
        """
        if gr.vertexes[v].dist > gr.vertexes[u].dist + gr.edges[(u, v)]:
            gr.vertexes[v].dist = gr.vertexes[u].dist + gr.edges[(u, v)]
            gr.vertexes[v].parent = gr.vertexes[u]
            v_queue[v] = gr.vertexes[v].dist

    def sw_dijkstra(self, gr, r_label):
        """
        Finds Shortest Way (SW) for the Graph by Dijkstra algorithm
        """
        r = gr.vertexes[r_label]
        r.dist = 0
        s_queue = dict()
        v_queue = {k: v.dist for k, v in gr.vertexes.items()}
        while v_queue:
            v_queue, u = self.extract_min(v_queue)
            s_queue[u] = gr.vertexes[u].dist
            for k, v in gr.vertexes[u].adj.items():
                self.relax(u, k, v_queue)

    def get_sw(self, gr, beg, end):
        sw = list()
        self.sw_dijkstra(gr, beg)
        v = gr.vertexes[end]
        path_len = v.dist
        while v:
            sw.append(v.label)
            v = v.parent
        return sw[::-1], path_len


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

    assert sol.get_sw(gr, 's', 'n') == (['s', 'x', 'z', 'n'], 9)

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
    gr.add_edge('x', 's', 7, False)

    # s -3- t -2- y -1- w
    #  \    |     |
    #   3   2     4
    #    \  |     |
    #      x  -5- z -3- n

    assert sol.get_sw(gr, 's', 'n') == (['s', 't', 'y', 'z', 'n'], 12)
