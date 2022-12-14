inpt = open("input.txt","r").read().strip()
lines = [[[int(k) for k in j.split(",")] for j in i.split("->")] for i in inpt.split("\n")] + [[[500,0]]]

def sign(n):
    if n == 0:
        return 0
    return n//abs(n)

def getCell(c):
    return grid[int(c.imag)-extrema[2]][int(c.real)-extrema[0]+1]

extrema = [0,\
           0,\
           min([min([j[1] for j in i]) for i in lines]),\
           max([max([j[1] for j in i]) for i in lines])]

ht = extrema[3]-extrema[2]
lines += [[[500-ht-10,extrema[3]+2],[500+ht+10,extrema[3]+2]]]

extrema[0] = 500-ht-10
extrema[1] = 500+ht+10

grid = [["." for x in range(extrema[1]-extrema[0]+2)] for y in range(extrema[3]-extrema[2]+3)]

for i in lines:
    for j in range(len(i)-1):
        start = complex(i[j][0],i[j][1])
        delta = complex(sign(i[j+1][0]-i[j][0]),sign(i[j+1][1]-i[j][1]))
        end =   complex(i[j+1][0],i[j+1][1])
        while start != end + delta:
            grid[int(start.imag)-extrema[2]][int(start.real)-extrema[0]+1] = "#"
            start += delta

moves = [1j,-1+1j,1+1j]
firstDropped = True
while getCell(500)==".":
    newgrain = 500
    while True:
        old = newgrain
        for i in moves:
            if getCell(newgrain+i) == ".":
                newgrain += i
                break
        if newgrain.real == old.real and newgrain.imag == old.imag:
            grid[int(newgrain.imag)-extrema[2]][int(newgrain.real)-extrema[0]+1] = "o"
            break
    if newgrain.imag > extrema[3]-1 and firstDropped:
        part1 = sum([y.count("o") for y in grid])
        print("Part 1:",part1)
        firstDropped = False
    sand = sum([y.count("o") for y in grid])
    if not firstDropped and sand%1000 == 0:
        print(sand,"/",extrema[3]**2)

for y in grid:
    print("".join(y))

print("Part 2:",sand)
