inpt = open("input.txt","r").read().strip()
inpt = [[int(j.split("=")[1]) for j in i.replace(":",",").split(",")] for i in inpt.split("\n")]
linenum = 2000000
searchrange = 4000000

def solveOverlaps(l):
    i, j = 0, 0
    while i < len(l):
        j=0
        while j < len(l):
            if i==j:
                j += 1
                continue
            if (l[i][0]<=l[j][0]<=l[i][1] or l[i][0]<=l[j][1]<=l[i][1]):
                l[i] = [min(l[i][0],l[j][0]),max(l[i][1],l[j][1])]
                l.pop(j)
                i = min(i,j)
                j = 0
            else:
                j += 1
        i += 1
    return l

def getRanges(y):
    ranges = []
    for i in inpt:
        coverage = abs(i[0]-i[2])+abs(i[1]-i[3])
        dist = abs(i[1]-y)
        if coverage > dist:
            overlap = coverage - dist
            ranges += [[i[0]-overlap,i[0]+overlap]]
    return ranges

part1 = solveOverlaps(getRanges(linenum))
print("Part 1:",sum([i[1]-i[0] for i in part1]))

candidates = []
for i in range(len(inpt)):
    for j in range(len(inpt)):
        if i==j:
            continue
        idist = abs(inpt[i][0]-inpt[i][2])+abs(inpt[i][1]-inpt[i][3])+1
        jdist = abs(inpt[j][0]-inpt[j][2])+abs(inpt[j][1]-inpt[j][3])+1
        for l in [[1,1],[-1,1],[1,-1],[-1,-1]]:
            a = inpt[i][1]+inpt[i][0]+l[0]*idist
            b = inpt[j][1]-inpt[j][0]+l[1]*jdist
            c = (a - b) // 2
            if abs(inpt[i][0]-c)+abs(inpt[i][1]-(c+b))==idist and 0<=c<=searchrange and 0<=(c+b)<=searchrange:
                candidates += [[c,c+b]]

for i in candidates:
    poss = True
    for j in inpt:
        if abs(j[0]-j[2])+abs(j[1]-j[3])>=abs(j[0]-i[0])+abs(j[1]-i[1]):
            poss = False
            break
    if poss:
        print("Part 2:",i[0]*4000000+i[1])
        break
