import copy 
import math 

def parse(filename) :
    D = {}
    with open(filename,'r') as f :
        for line in f :
            source, direction, poid = line.strip().split(',')
            if source in D : 
                D[source][direction] = int(poid)
            else :
                D[source] = {}
                D[source][direction] = int(poid)

    return(D)

def number_vertices(G) :
    S = set()
    for (key,value) in G.items() :
        S.add(key)
        S.update(list(value.keys()))
    return(len(S))
    
dict = parse("graph.csv")
print(number_vertices(dict))
print(dict)


def reachables(graph,s) :
    
    S = set() #liste des sommets déjà visité, variable globale

    def aux(graph,t) :
        
        if t not in graph and t not in S:
            S.add(t)
        elif t in graph and t not in S: 
            S.add(t)
            for x in graph[t] :
                aux(graph,x)
    aux(graph,s)
    return(S)

def shortest_distance(graph,v1,v2) : 
    
    visited = {v1 : 0}

    while True :     
        
        edges = set()

        for source, marque in visited.items() :
            adj = graph[source]
            for d, w in adj.items() :
                if v2 in reachables(graph,d) and d not in visited :
                    edges.add((d, marque + w))
        
        if not edges :
            return(None)
        
        
        shortest_length = math.inf
        shortest_vertex = None
        for edge in edges:
            if edge[1] < shortest_length :
                shortest_length = edge[1]
                shortest_vertex = edge[0]
        
        if shortest_vertex == v2 :
            return(shortest_length)
        else :
            visited[shortest_vertex] = shortest_length
    

G2 = {'v1': {'v3': 5, 'v2': 1},
 'v2': {'v3': 1, 'v4': 3, 'v5': 4},
 'v3': {'v4': 1},
 'v4': {'v5': 1, 'v6': 3},
 'v5': {'v6': 1}}

print(shortest_distance(dict,'a','f'))

def shortest_path(graph,v1,v2) :
    visited = {v1 : [0,v1]}

    while True :     
        
        edges = set()

        for source, marque in visited.items() :
            adj = graph[source]
            for d, w in adj.items() :
                if v2 in reachables(graph,d) and d not in visited :
                    edges.add((d, marque[0] + w, tuple(marque[1:])))
        
        if not edges :
            return(None)
        
        
        shortest_length = math.inf
        shortest_vertex = None
        chemin = []
        for edge in edges:
            if edge[1] < shortest_length :
                shortest_length = edge[1]
                shortest_vertex = edge[0]
                chemin = list(edge[2])      
        
        
        if shortest_vertex == v2 :
            return((shortest_length, chemin + [v2]))
        else :
            visited[shortest_vertex] = [shortest_length] + chemin + [shortest_vertex]


