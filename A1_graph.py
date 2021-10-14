from math import inf


class Vertex:
    def __init__(self, label):
        self.label = label
        self.adj = dict()       # dictionary of adjacent vertexes
        self.color = 'white'
        self.dist = inf         # distance to vertex from initial vertex
        self.parent = None      # parent vertex
        self.t_b = 0            # time of first meet by DFS algo
        self.t_f = 0            # time of last meet by DFS algo


class Edge:
    def __init__(self, begin, end, weight):
        self.begin = begin
        self.end = end
        self.weight = weight


class Graph:
    def __init__(self, vertexes=None):
        self.vertexes = dict()
        self.edges = dict()
        if vertexes:
            for v in vertexes:
                self.vertexes[v] = Vertex(v)

    def add_vertex(self, v):
        if v not in self.vertexes:
            self.vertexes[v] = Vertex(v)
            return True
        return False

    def add_edge(self, v_begin, v_end, weight, oriented=True):
        if v_begin in self.vertexes and v_end in self.vertexes:
            self.vertexes[v_begin].adj[v_end] = weight
            self.edges[(v_begin, v_end)] = weight
            if not oriented:
                self.vertexes[v_end].adj[v_begin] = weight
                self.edges[(v_end, v_begin)] = weight
            return True
        return False

    def print_graph(self):
        for k, v in self.vertexes.items():
            print(f'{k} -> {v.adj}')


if __name__ == '__main__':
    gr = Graph(['s', 't', 'x', 'y', 'z'])
    gr.add_vertex('s')
    gr.add_vertex('w')
    gr.add_edge('s', 't', 6)
    gr.add_edge('s', 'y', 7)
    gr.add_edge('t', 'x', 5)
    gr.add_edge('t', 'y', 8)
    gr.add_edge('t', 'z', 2)
    gr.add_edge('x', 't', 3)
    gr.add_edge('y', 'x', 4)
    gr.add_edge('y', 'z', 9)
    gr.add_edge('z', 's', 2)
    gr.add_edge('z', 'x', 7)
    gr.add_edge('w', 't', 5)
    gr.add_edge('w', 'y', 3)
    gr.add_edge('w', 'y', 5)
    gr.add_edge('w', 'z', 6)
    gr.print_graph()


