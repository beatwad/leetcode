from A1_graph import Graph
from math import inf


class Solution:
    def bfs(self, gr: Graph, s) -> None:
        """
        Breadth First Search in Graph
        :param gr: Graph
        :param s: int or str
        :return: None
        """
        for v in gr.vertexes.values():
            v.color = 'white'
            v.dist = inf
            v.parent = None
        root = gr.vertexes[s]
        root.color = 'gray'
        root.dist = 0
        root.parent = None
        queue = list()
        queue.append(root)
        while queue:
            u = queue.pop()
            for k, v in u.adj.items():
                vert = gr.vertexes[k]
                if vert.color == 'white':
                    vert.color = 'gray'
                    vert.dist = u.dist + 1
                    vert.parent = u
                    queue.append(vert)

    def path(self, gr: Graph, v_end):
        """
        Shows path from initial vertex of Graph to another vertex
        :param gr: Graph
        :param v_end: int or str
        :return: list[int] or list[str]
        """
        v = gr.vertexes[v_end]
        s_path = list()
        while v:
            s_path.append(v.label)
            v = v.parent
        return s_path[::-1]


if __name__ == '__main__':
    sol = Solution()

    gr = Graph(['s', 't', 'x', 'y', 'z'])
    gr.add_vertex('s')
    gr.add_vertex('w')
    gr.add_edge('s', 't', 1, False)
    gr.add_edge('t', 'x', 1, False)
    gr.add_edge('t', 'y', 1, False)
    gr.add_edge('z', 'y', 1, False)
    gr.add_edge('y', 'w', 1, False)

    # s -- t -- y -- w
    #      |    |
    #      x    z

    sol.bfs(gr, 's')
    assert gr.vertexes['w'].dist == 3
    assert sol.path(gr, 'w') == ['s', 't', 'y', 'w']

    sol.bfs(gr, 'y')
    assert gr.vertexes['w'].dist == 1
    assert sol.path(gr, 's') == ['y', 't', 's']

    sol.bfs(gr, 'x')
    assert gr.vertexes['s'].dist == 2
    assert sol.path(gr, 'x') == ['x']
    assert sol.path(gr, 'w') == ['x', 't', 'y', 'w']
