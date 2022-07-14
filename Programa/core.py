import pandas as pd

INFINITY = 2.0**50.0

class Graph:
    def __init__(self, v_data_path="vertexs.csv", e_data_path="arestes.csv"):
        data = pd.read_csv(v_data_path, names=['LATITUD', 'LONGITUD'], sep=",", comment="#")
        vertex_data = tuple(zip(data['LATITUD'].values, data['LONGITUD'].values))

        data_edge = pd.read_csv(e_data_path, names=['ORIGEN', 'DESTI', 'PES'], sep=",", comment="#")
        edge_data = tuple(zip(data_edge['ORIGEN'].values, data_edge['DESTI'].values, data_edge['PES'].values))
        
        self.vertices = int(data.size/2) #It is a tuple, so data is 2n but the vertex count is n
        self.edges = {int:list[int]}
        self.weight = {int:{int:float}}

        self.vertex_coord = {int:(float,float)}

        #Based on the data(pos) in the csv file, we can know how many vertices there are, their positions and initislize
        #both the adjacency list and the weight matrix.
        index = 1
        for d in vertex_data:
            self.edges.update({index:[]})
            self.vertex_coord[index] = d
            for j in range(1, self.vertices+1):
                self.weight.update({index:{j:INFINITY}})
            index += 1
        index = 1
        for d in edge_data:
            o,g,w = d
            self.set_edge(o,g,w)
            index +=1          
    
    def set_edge(self, v0: int, vf: int, w: float):
        self.edges[v0].append(vf)
        self.weight[v0][vf]=w
    
    def set_vertex_coord(self, index, pos: tuple[float,float]):
        self.vertex_coord.update({index:pos})

#FIXME: Aquesta funció heurística és per al mode de busca ràpida normal
#       per això retorna només la distància euclidiana entre les posicions
#       EL QUE S'HA DE FER ARA ÉS CREAR-NE UNA QUE TINGUI EN COMPTE LES VALORACIONS
#       AL INSTAGRAM COM A PART DE LA FUNCIÓ.
#
#FIXME: ALGORITME RUTA (UTILITZARÀ A*): SELECCIONES EL TIPUS DE LLOC QUE VOLS VISITAR
#       TROBA ELS VÈRTEXS QUE COMPLEIXIN AQUESTA CONDICIÓ I BUSCA EL CAMÍ MÉS CURT
#       ENTRE ELLS I ELS UNEIX (DONARÀ COM A RESULTAT EL CAMÍ MÉS CURT D'UN EXTREM A UN ALTRE PASSANT PER TOTS ELS MARCATS)
#       POSTERIORMENT, BUSCA EL CAMÍ MÉS CURT ENTRE LA TEVA POSICIÓ I UN VÈRTEX EXTREM I L'ADHEREIX A LA RUTA
def h_test(v: tuple[float, float], goal: tuple[float, float]) -> float:
    x1, y1 = v
    x2, y2 = goal
    return ((x2-x1)**2+(y2-y1)**2)**0.5

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

def A_Star(g: Graph, src: int, goal: int, h=h_test) -> list[int]:
    openSet = [src]
    comeFrom = {}
    gScore = {}
    fScore = {}
    for i in range(1,g.vertices+1):
        gScore[i] = INFINITY
        fScore[i] = INFINITY
    gScore[src] = 0
    fScore[src] = h(g.vertex_coord[src], g.vertex_coord[goal])

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
                fScore[w] = tentative_gScore+h(g.vertex_coord[w], g.vertex_coord[goal])
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