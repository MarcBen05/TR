#Es crea un graf de 6 vertexs. (Aquest graf es en forma de llista d'adjacencia)
graph = {}
graph[1] = {2,5}
graph[2] = {1,3}
graph[3] = {2}
graph[4] = {5}
graph[5] = {1,4,6}
graph[6] = {5}

# S'empren variables globals ja que al ser una funcio recursiva aquesta estaria creant variables
# noves tota l'estona
e = {}
for i in graph.keys():
    e[i] = False
q = []

def DFS_recursive(graph, v, explored):
    global q
    explored[v] = True
    for w in graph[v]:
        if explored[w] == False:
            q.append(w)
            DFS_recursive(graph,w, explored)

DFS_recursive(graph, 1, e)
print(q)