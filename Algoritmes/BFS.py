#Es crea un graf de 6 vertexs. (Aquest graf es en forma de llista d'adjacencia)
graph = {}
graph[1] = {2,5}
graph[2] = {1,3}
graph[3] = {2}
graph[4] = {5}
graph[5] = {1,4,6}
graph[6] = {5}

#Aquesta funcio ens diu si dos vertexs d'un graf son adjacents
def IsAdjacent(graph, p, c):
    for i in graph[p]:
        if (c == i):
            return True
    return False

def BFS(graph1, src, goal):
    #Si l'origen i el final son iguals no cal fer res
    if (src == goal):
        return src

    q = [] #Cua per a processar vertexs
    current_path = [] #Llista on afegim els vertexs que hem explorat
    explored = {} #Diccionari que ens diu si un vertex ha estat explorat

    #Aqui marquem tots els vertexs com a no explorats
    for i in graph1.keys():
        explored[i] = False

    explored[src] = True #Marquem el vertex origen com a explorat
    q.append(src)
    while q:
        v = q.pop(0)
        current_path.append(v)
        if v == goal:
            path = [] #Llista amb el cami final
            current_node = v #Aquesta variable indica quin vertexs estem processant del cami
            index = len(current_path) - 1 #Obtenim la llargada dels vertexs explorats
            while index > -1:
                # Aquesta funcio revisa els vertexs explorats des del final cap a l'origen.
                if IsAdjacent(graph1, current_path[index],current_node):
                # Si el vertex actual es adjacent a l'anterior en la llista, vol dir que forma
                # part del cami.
                # Per tant s'afegeix el vertex al cami final i el vertex a processar sera el
                # que era adjacent.
                    current_node = current_path[index]
                    path.append(current_path[index])

                current_path.pop()
                index = index - 1 # L'index de la llista disminueix
            
            path.reverse() # Girem la llista ja que l'ordre era invers
            path.append(goal) # S'afegeix el vertex final ja que s'ha ignorat
            return path

        for w in graph1[v]:
            if explored[w] == False:
                explored[w] = True
                q.append(w)
    
    return []

print(BFS(graph, 2,6))