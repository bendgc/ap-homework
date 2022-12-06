
def parse(filename) :
    L = list()
    with open(filename,'r') as f : 
        for line in f : 
            l = line.split()
            person = {}
            person['first_name'] = l[0]
            person['last_name'] = l[1]
            person['bithday'] = (l[2],l[3],l[4])
            L.append(person)
    return(L)

def index(L) :
    return({
        (person['first_name'],person['last_name']) 
        for person in L
    })


def nb_first_names(L):
    S = set()
    for person in L :
        S.add(person['first_name'])
    return(len(S))

