def extract_minimum(q, dist):
    v = 0
    prev_dist = INFINITY
    for w in q:
        if dist[w] < prev_dist:
            prev_dist = dist[w]
            v = w
    q.remove(v)
    return v

def Dijkstra(graph, weight, src):
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

    while q:
        v = extract_minimum(q, dist)
        visited[v] = True
        for w in graph[v]:
            if visited[w] == False:
                if dist[w] > dist[v] + weight[v][w]:
                    dist[w] = dist[v] + weight[v][w]
                    parent[w] = v
                    q.append(w)
    #Ens imprimeix cada vertex, el seu pare i el valor de la seva connexio
    for v in graph.keys():
        if parent[v] != 0:
            print(f"El vertex {v} te el pare: {parent[v]}. {parent[v]}{v}={weight[parent[v]][v]}")