import random as rd
import time 

start = time.time()

D = set()
date = []
n = 10000
count = 0
filename1 = 'last_names.txt'
filename2 = 'first_names.txt'

with open(filename1,'r') as g :
    with open(filename2,'r') as f :
        first = f.readlines()
        last = g.readlines()
        while count < n :
            name1 = rd.choice(first).strip()
            name2 = rd.choice(last).strip()
            if not f"{name1} {name2}" in D :
                D.add(f"{name1} {name2}")
                count += 1
                date.append(str(rd.randint(0,28))+'/' + str(rd.randint(0,12)) + '/' + str(rd.randint(2000,2004)))
    

with open("data-big.txt",'w') as f :
    for name , d in zip(D,date) :
        f.write(f"{name} {d}" + "\n")

end = time.time()
time_tot = str(end-start)

print(time_tot)
