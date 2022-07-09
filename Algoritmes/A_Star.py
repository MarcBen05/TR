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

# Aquesta funcio heuristica es arbitraria, si s'escolleix aquest
# algoritme s'ha de dissenyar una millor
def h(u):
    return int((u+1)**0.5)

def reconstruct_path(comeFrom, current):
    total_path = [current]
    while current in comeFrom.keys():
        current = comeFrom[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

def extract_minimum(openSet, fScore):
    min_val = 0
    min_score = INFINITY
    for i in openSet:
        if (fScore[i] < min_score):
            min_val = i
            min_score = fScore[i]
    return min_val

def A_Star(graph, weight, src, goal, h):
    openSet = [src]
    comeFrom = {}
    gScore = {}
    fScore = {}
    for i in graph.keys():
        gScore[i] = INFINITY
        fScore[i] = INFINITY
    gScore[src] = 0
    fScore[src] = h(src)
    while openSet:
        current = extract_minimum(openSet, fScore)
        if current == goal:
            return reconstruct_path(comeFrom, current)
        openSet.remove(current)
        for w in graph[current]:
            tentative_gScore = gScore[current]+weight[current][w]
            if tentative_gScore < gScore[w]:
                comeFrom[w] = current
                gScore[w] = tentative_gScore
                fScore[w] = tentative_gScore+h(w)
                if not w in openSet:
                    openSet.append(w)
    return []

print(A_Star(graph, weight, 2, 6, h))