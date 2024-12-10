class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        print()
        for i in self.adj_list:
            print(f"{i} : {self.adj_list[i]}")

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        '''bidirectional connection'''
        # edge case
        if not v1 in self.adj_list or not v2 in self.adj_list or v1 == v2:
            return False

        # vertexes connection
        if not v2 in self.adj_list[v1] and not v1 in self.adj_list[v2]:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True

        
        

my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.print_graph()

my_graph.add_edge("A", "D")
my_graph.print_graph()
my_graph.add_edge("B", "C")
my_graph.print_graph()
my_graph.add_edge("B", "D")
my_graph.print_graph()
my_graph.add_vertex("H")
my_graph.add_edge("H", "B")
my_graph.add_edge("H", "A")
my_graph.print_graph()
my_graph.add_edge("C", "H")
my_graph.print_graph()










