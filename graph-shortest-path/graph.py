import copy 

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


