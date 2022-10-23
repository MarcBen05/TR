#Es crea un graf de 6 vertexs. (Aquest graf es en forma de llista d'adjacencia)
graph = {}
graph[1] = {2,5}
graph[2] = {1,3}
graph[3] = {2,4}
graph[4] = {3,5}
graph[5] = {1,4,6}
graph[6] = {5}

def DFS(graph, src):
    e = {}
    for i in graph.keys():
        e[i] = False
    s = []
    q = []
    s.append(src)
    while s:
        v = s.pop()
        if e[v] == False:
            q.append(v)
            e[v] = True
            for w in graph[v]:
                s.append(w)
    print(q)




DFS(graph, 1)