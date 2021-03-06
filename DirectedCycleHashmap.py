
class Graph(object):

    def __init__(self, is_directed):
        self.all_edges = []
        self.all_vertex = {}
        self.is_directed = is_directed

    def add_edge(self, id1, id2, weight=0):
        if id1 in self.all_vertex:
            vertex1 = self.all_vertex[id1]
        else:
            vertex1 = Vertex(id1)
            self.all_vertex[id1] = vertex1

        if id2 in self.all_vertex:
            vertex2 = self.all_vertex[id2]
        else:
            vertex2 = Vertex(id2)
            self.all_vertex[id2] = vertex2

        edge = Edge(vertex1, vertex2, self.is_directed, weight)
        self.all_edges.append(edge)
        vertex1.add_adjacent_vertex(edge, vertex2)
        if self.is_directed is not True:
            vertex2.add_adjacent_vertex(edge,vertex1)

 
class Edge(object):
    
    def __init__(self, vertex1, vertex2, is_directed, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.is_directed = is_directed
        self.weight = weight

    def __eq__(self, other):
        return self.vertex1.id == other.vertex1.id and self.vertex2.id == other.vertex2.id

    def __hash(self):
        return hash(vertex1) + hash(vertex2)
    
    def __str__(self):
        return "Edge " + str(self.vertex1) + " " + str(self.vertex2) + " Weight-" + str(self.weight)

    def __repr__(self):
        return self.__str__()
    
class Vertex(object):

    def __init__(self, id):
        self.id = id;
        self.edges = []
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, edge, vertex):
        self.edges.append(edge)
        self.adjacent_vertices.append(vertex)

    def get_degree(self):
        return len(self.edges)

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return str("Vertex-" + str(self.id))

    def __repr__(self):
        return self.__str__();

    def __lt__(self, other):
        return self.id < other.id
                    
    def __gt__(self, other):
        return self.id > other.id
#=========================================================================== main code 
def has_cycle(graph):
  white = set()
  gray = set()
  black = set()

  for vertex in graph.all_vertex.values():
    white.add(vertex)
  while len(white) > 0:
    current = next(iter(white))
    if dfs(current,white, gray, black) == True:
      return True
  return False

def dfs(current, white, gray, black):
  move_vertex(current, white, gray )
  for neighbor in current.adjacent_vertices:
    if neighbor in black:
      continue
    if neighbor in gray:
      return True
    if dfs(neighbor, white, gray, black) == True:
      return True
  move_vertex(current, gray, black)
  return False

def move_vertex(vertex, source_set, destination_set):
  source_set.remove(vertex)
  destination_set.add(vertex)
if __name__ == '__main__':
    graph = Graph(True)
    graph.add_edge(1,2)
    graph.add_edge(1,3)
    graph.add_edge(2,3)
    graph.add_edge(4,1)
    graph.add_edge(4,5)
    graph.add_edge(5,6)
    graph.add_edge(6,4)

    print(has_cycle(graph));
