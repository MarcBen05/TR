#Es crea un graf de 6 vertexs. (Aquest graf es en forma de llista d'adjacencia)
graph = {}
graph[1] = {2,5}
graph[2] = {1,3}
graph[3] = {2}
graph[4] = {5}
graph[5] = {1,4,6}
graph[6] = {5}

def IsAdjacent(graph, p, c):
    for i in graph[p]:
        if (c == i):
            return True
    return False

def DFS_find_path(graph, src, goal):
    if (src == goal):
        print(src)
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

                #Com a l'algoritme BFS, una vegada s'ha trobat
                # el vertex desitjat es construeix un cami amb
                # els vertexs adjacents fins a l'origen.
                if (w == goal):
                    final_path = []
                    q.reverse()
                    current_node = w
                    for i in q:
                        if IsAdjacent(graph, i, current_node):
                            final_path.append(i)
                            current_node = i

                    final_path.reverse()
                    final_path.append(goal)
                    return final_path
                s.append(w)

print(DFS_find_path(graph, 1, 3))