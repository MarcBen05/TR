INFINITY = 2**50

class Graph:
    def __init__(self, n: int):
        self.vertices = n
        self.positions = {int:[float, float]}
        self.edges = {int:list[int]}
        self.weight = {int:{int:int}}

        for i in range(1,n+1):
            self.edges.update({i:[]})
            for j in range(1,n+1):
                self.weight.update({i:{j:INFINITY}})
    
    def set_edge(self, v0: int, vf: int, w: int):
        self.edges[v0].append(vf)
        self.weight[v0][vf]=w
    
    def set_node_pos(self, index: int, x: float, y:float):
        self.positions[index] = [x, y]

#FIXME: Returns euclidean distance from the window atm. Should
        #take weight(distance) into account, not just windowPos.
def h(v: list[float], goal: list[float]) -> float:
    return ((goal[0]-v[0])**2+(goal[1]-v[1])**2)**0.5

def reconstruct_path(comeFrom: dict[int:int], current: int) -> list[int]:
    total_path = [current]
    while current in comeFrom.keys():
        current = comeFrom[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

def extract_minimum(openSet: list[int], fScore: dict[int:float]) -> int:
    min_val = 0
    min_score = INFINITY
    for i in openSet:
        if (fScore[i] < min_score):
            min_val = i
            min_score = fScore[i]
    return min_val

def A_Star(g: Graph, src: int, goal: int, h) -> list[int]:
    openSet = [src]
    comeFrom = {}
    gScore = {}
    fScore = {}
    for i in range(1,g.vertices+1):
        gScore[i] = INFINITY
        fScore[i] = INFINITY
    gScore[src] = 0
    fScore[src] = h(g.positions[src], g.positions[goal])

    while openSet:
        current = extract_minimum(openSet, fScore)
        if current == goal:
            return reconstruct_path(comeFrom, current)
        openSet.remove(current)
        for w in g.edges[current]:
            tentative_gScore = gScore[current]+g.weight[current][w]
            if tentative_gScore < gScore[w]:
                comeFrom[w] = current
                gScore[w] = tentative_gScore
                fScore[w] = tentative_gScore+h(g.positions[w],g.positions[goal])
                if not w in openSet:
                    openSet.append(w)
    return []

"""
API EXAMPLE
g = Graph(6)
g.set_edge(1,2,1)
g.set_edge(1,5,2)
g.set_edge(2,3,3)
g.set_edge(3,4,2)
g.set_edge(4,5,7)
g.set_edge(5,6,4)

for i in range(1,g.vertices+1):
    if (i%2) == 0:
        g.set_node_pos(i, i, 0)
    else:
        g.set_node_pos(i, i, 1)

print(A_Star(g,2,6,h))
"""