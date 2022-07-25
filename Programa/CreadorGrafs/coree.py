import pandas as pd
import numpy as np

INFINITY = 2.0**50.0

class Graph:
    def __init__(self, v_data_path="vertexs.csv", e_data_path="arestes.csv"):
        data = pd.read_csv(v_data_path, names=['LATITUD', 'LONGITUD', 'CATEGORIA'], sep=",", comment="#")
        data['CATEGORIA'] = data['CATEGORIA'].astype('|S')
        vertex_data = tuple(zip(data['LATITUD'].values, data['LONGITUD'].values, data['CATEGORIA'].values))

        data_edge = pd.read_csv(e_data_path, names=['ORIGEN', 'DESTI', 'PES'], sep=",", comment="#")
        edge_data = tuple(zip(data_edge['ORIGEN'].values, data_edge['DESTI'].values, data_edge['PES'].values))
        
        self.vertices = int(data.size/2) #It is a tuple, so data is 2n but the vertex count is n
        self.edges = {int:list[int]}
        self.weight = {int:{int:float}}

        self.vertex_coord = {}
        # 1->Monument, 2->Museu, 3-> Lloc emblematic, 4->Parc, 5->Oci nocturn, 6->Lloc popular insta, 7->Exposicions, 8->Atraccions turistiques
        self.vertex_caract = {}

        #Based on the data(pos) in the csv file, we can know how many vertices there are, their positions and initislize
        #both the adjacency list and the weight matrix.
        index = 1
        for d in vertex_data:
            x,y,z = d
            self.edges.update({index:[]})
            self.vertex_caract.update({index:[]})
            self.vertex_coord[index] = (x,y)
            #Assignar les categories a cada vertex
            if z.decode('UTF-8') != 'nan':
                for c in z.decode('UTF-8')[:-2]:
                    self.vertex_caract[index].append(c)
            #Assignar totes les distancies a infinit
            for j in range(1, self.vertices+1):
                self.weight.update({index:{j:INFINITY}})
            index += 1
        
        #Assignar les arestes amb els seus pesos
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

    def find_closest(self,coord) -> int:
        x1,y1 = coord
        return min(self.vertex_coord, key=lambda x:abs(((x1-self.vertex_coord[x][0])**2+(y1-self.vertex_coord[x][1])**2)**0.5))
    
    def route_to_coords(self, route):
        coord = []
        for i in route:
            coord.append(self.vertex_coord[i])
        return coord

    def find_vertices_with_tag(self, tag: str):
        vertices = []

        for k in self.vertex_caract.keys():
            if self.vertex_caract[k]:
                for i in self.vertex_caract[k]:
                    if i == tag:
                        vertices.append(k)

        return vertices

    def find_vertices_with_tags(self, tags: list[str]):
        vertices = []
        subset = set(tags)
        for k in self.vertex_caract.keys():
            if self.vertex_caract[k]:
                if subset.issubset(set(self.vertex_caract[k])):
                    vertices.append(k)

        return vertices


#FIXME: ALGORITME RUTA (UTILITZARÀ Dijkstra): SELECCIONES EL TIPUS DE LLOC QUE VOLS VISITAR
#       TROBA ELS VÈRTEXS QUE COMPLEIXIN AQUESTA CONDICIÓ I BUSCA EL CAMÍ MÉS CURT
#       ENTRE ELLS I ELS UNEIX (DONARÀ COM A RESULTAT EL CAMÍ MÉS CURT D'UN EXTREM A UN ALTRE PASSANT PER TOTS ELS MARCATS)
#       POSTERIORMENT, BUSCA EL CAMÍ MÉS CURT ENTRE LA TEVA POSICIÓ I UN VÈRTEX EXTREM I L'ADHEREIX A LA RUTA

#FIXME: Carregar dos grafs inicialment: cotxe(dirigit) i peu(simple). Depenent de que escolleixi l'usuari,
#       emprarem un o l'altre

def extract_minimum(q, dist):
    v = 0
    prev_dist = INFINITY
    for w in q:
        if dist[w] < prev_dist:
            prev_dist = dist[w]
            v = w
    q.remove(v)
    return v

def Dijkstra(g:Graph, src: int, goal: int) -> tuple[list[int], float]:
    dist = {}
    visited = {}
    parent = {}
    q = []

    for i in g.edges.keys():
        dist[i] = INFINITY
        parent[i] = 0
        visited[i] = False
    dist[src] = 0
    q.append(src)
    visited[src] = True

    while q:
        v = extract_minimum(q, dist)
        visited[v] = True

        if (v == goal):
            weight = dist[goal]
            path = []
            u = v
            if parent[u] != 0 or u == src:
                while u != 0:
                    path.insert(0, u)
                    u = parent[u]
            return (path, weight)

        for w in g.edges[v]:
            if visited[w] == False:
                if dist[w] > dist[v] + g.weight[v][w]: #Les llistes son base comencen per 0 i w comença per 1
                    dist[w] = dist[v] + g.weight[v][w]
                    parent[w] = v
                    q.append(w)
    return ([], 0)

#region Dijkstra_Restricted
def Dijkstra_Restricted(g:Graph, src: int, goal: int, restriction:dict) -> tuple[list[int], float, dict]:
    dist = {}
    visited = {}
    parent = {}
    q = []

    for i in g.edges.keys():
        dist[i] = INFINITY
        parent[i] = 0
        visited[i] = False

    if len(restriction) != 0:
        for i in restriction.keys():
            visited[i] = restriction[i]
    
    dist[src] = 0
    q.append(src)
    visited[src] = True

    while q:
        v = extract_minimum(q, dist)
        visited[v] = True

        if (v == goal):
            weight = dist[goal]
            path = []
            u = v
            if parent[u] != 0 or u == src:
                while u != 0:
                    path.insert(0, u)
                    u = parent[u]
            restr = {}
            for i in path:
                restr[i]=True
            return (path, weight, restr)

        for w in g.edges[v]:
            if visited[w] == False:
                if dist[w] > dist[v] + g.weight[v][w]: #Les llistes son base comencen per 0 i w comença per 1
                    dist[w] = dist[v] + g.weight[v][w]
                    parent[w] = v
                    q.append(w)
    return ([], 0, {})

#endregion

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
"""