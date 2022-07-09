#Es crea un graf de 6 vertexs. (Aquets graf es en forma de llista d'adjacencia)
graph = {}
graph[1] = {2,5}
graph[2] = {1,3}
graph[3] = {2,4}
graph[4] = {3,5}
graph[5] = {1,4,6}
graph[6] = {5}

def IsAdjacent(graph, p, c):
    for i in graph[p]:
        if (c == i):
            return True
    return False

def DFS_recursive(graph, src, goal, current_depth):
    global e # S'empren variables globals ja que al ser una funcio recursiva aquesta estaria
    global s #  creant variables noves tota l'estona
    global q

    # Aqui mirem que la profunditat actual sigui major o igual a 0 per a que no hi hagi una recursio infinita.
    if (current_depth >= 0):
        for w in graph[src]:
            if e[w] == False:
                e[w] = True
                if w == goal:
                    q.append(w)
                    return True
                if DFS_recursive(graph, w, goal, current_depth-1) == True:
                    q.append(w)
                    return True
    for i in graph.keys():
        e[i] = False  # Desmarquem tots els vertexs explorats per a la proxima iteracio
    return False

def DFS_shortest_path(graph, src, goal, max_depth):
    if (src == goal):
        print(src)
        return
    depth = 0
    v = src
    # Aqui comencem amb l'aprofundiment iteratiu.
    while depth < max_depth:
        if DFS_recursive(graph, src, goal, depth) == True:
            q.append(src)
            q.reverse() # Invertim la llista per a que l'ordre sigui correcte
            print(f"S'ha trobat un cami! -> {q}")
            return
        depth = depth + 1
            
    print(f"No s'ha trobat cap cami. Pot ser mes llarg de {max_depth} o no existeix")

e = {}
for i in graph.keys():
    e[i] = False
s = []
q = []
depth = 0

DFS_shortest_path(graph, 3, 6, 2)