INFINITY = 2**50
#Graf
graph = {}
graph[1] = {2,5}
graph[2] = {1,3}
graph[3] = {2,4}
graph[4] = {3,5}
graph[5] = {1,4,6}
graph[6] = {5}

#Matriu de pesos del graf
weight = {}
weight[1] = {1:INFINITY,   2:1,            3:INFINITY, 4:INFINITY, 5:2,        6:INFINITY}
weight[2] = {1:1,          2:INFINITY,     3:3,        4:INFINITY, 5:INFINITY, 6:INFINITY}
weight[3] = {1:INFINITY,   2:3,            3:INFINITY, 4:2,        5:INFINITY, 6:INFINITY}
weight[4] = {1:INFINITY,   2:INFINITY,     3:2,        4:INFINITY, 5:7,        6:INFINITY}
weight[5] = {1:2,          2:INFINITY,     3:INFINITY, 4:7,        5:INFINITY, 6:4}
weight[6] = {1:INFINITY,   2:INFINITY,     3:INFINITY, 4:INFINITY, 5:4,        6:INFINITY}

#Funcio per extreure l'element amb menor distancia de la cua
def extract_minimum(q, dist):
    v = 0
    prev_dist = INFINITY
    for w in q:
        if dist[w] < prev_dist:
            prev_dist = dist[w]
            v = w
    q.remove(v)
    return v

def Dijkstra(graph, weight, src, goal):
    dist = {}
    visited = {}
    parent = {}
    q = []

    for i in graph.keys():
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
            path = []
            u = v
            if parent[u] != 0 or u == src:
                while u != 0:
                    path.insert(0, u)
                    u = parent[u]
            return path

        for w in graph[v]:
            if visited[w] == False:
                if dist[w] > dist[v] + weight[v][w]: #Les llistes son base comencen per 0 i w comença per 1
                    dist[w] = dist[v] + weight[v][w]
                    parent[w] = v
                    q.append(w)
    return []

print(Dijkstra(graph, weight, 5, 3))