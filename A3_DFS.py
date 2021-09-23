from A1_graph import Graph
from A1_graph import Vertex


class Solution:
    def __init__(self):
        self.time = 0

    def dfs(self, gr: Graph) -> None:
        """
        Depth First Search in Graph
        :param gr: Graph
        :return: None
        """
        for u in gr.vertexes.values():
            u.color = 'white'
            u.parent = None
        self.time = 0

        for u in gr.vertexes.values():
            if u.color == 'white':
                self.dfs_visit(gr, u)

    def dfs_visit(self, gr: Graph, u: Vertex) -> None:
        """
        DFS helper function
        :param gr: Graph
        :param u: Vertex
        :return: None
        """
        self.time += 1
        u.t_b = self.time
        u.color = 'gray'
        for k, v in u.adj.items():
            vert = gr.vertexes[k]
            if vert.color == 'white':
                vert.parent = u
                self.dfs_visit(gr, vert)
        u.color = 'black'
        self.time += 1
        u.t_f = self.time

    def find_strong_conn_components(self, gr) -> list:
        """
        Function for finding of strongly connected components of Graph
        :param gr: Graph
        :return: list[list[int]] or list[list[str]]
        """
        self.dfs(gr)
        scc = list()
        for u in gr.vertexes.values():
            for s in scc:
                if (u.t_b < s[1][0] and u.t_f > s[1][1]) or (u.t_b > s[1][0] and u.t_f < s[1][1]):
                    s[0].append(u.label)
                    s[1][0] = min(s[1][0], u.t_b)
                    s[1][1] = max(s[1][1], u.t_f)
                    break
            else:
                scc.append([[u.label], [u.t_b, u.t_f]])
        return [s[0] for s in scc]


if __name__ == '__main__':
    sol = Solution()

    gr = Graph(['s', 't', 'x', 'y', 'z', 'w', 'k', 'l', 'm', 'o', 'n'])
    gr.add_edge('s', 't', 1, True)
    gr.add_edge('t', 'x', 1, True)
    gr.add_edge('t', 'y', 1, True)
    gr.add_edge('y', 'z', 1, True)
    gr.add_edge('y', 'w', 1, True)
    gr.add_edge('k', 'l', 1, True)
    gr.add_edge('l', 'o', 1, True)
    gr.add_edge('z', 'n', 1, True)

    # s -- t -- y -- w    k -- l    m
    #      |    |              |
    #      x    z -- n         o

    assert sol.find_strong_conn_components(gr) == [['s', 't', 'x', 'y', 'z', 'w', 'n'], ['k', 'l', 'o'], ['m']]
