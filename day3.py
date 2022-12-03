inpt = open("input.txt","r").read().strip()
prios = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def union(a,b):
    c = [n for n in a if n in b]
    return c

compartments = [[i[:len(i)//2],i[len(i)//2:]] for i in inpt.split("\n")]
overlap = [union(set(i[0]),set(i[1]))[0] for i in compartments]
print("Part 1:",sum([prios.index(i) for i in overlap]))

groups = [inpt.split("\n")[i:i+3] for i in range(0,inpt.count("\n"),3)]
badges = [union(union(set(i[0]),set(i[1])),set(i[2]))[0] for i in groups]
print("Part 2:",sum([prios.index(i) for i in badges]))
