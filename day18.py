inpt = open("input.txt","r").read().strip()
cubes = [[int(j) for j in i.split(",")] for i in inpt.split("\n")]

def getSurface(l):
    adjs = 0
    for i in l:
        for j in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
            if [i[0]+j[0],i[1]+j[1],i[2]+j[2]] in l:
                adjs += 1
    return 6*len(l)-adjs

p1 = getSurface(cubes)
print("Part 1:",p1)

bounds = [[min([i[0] for i in cubes])-1,min([i[1] for i in cubes])-1,min([i[2] for i in cubes])-1],\
          [max([i[0] for i in cubes])+1,max([i[1] for i in cubes])+1,max([i[2] for i in cubes])+1]]

air = []
queue = [bounds[0]]
while len(queue)>0:
    point = queue.pop(0)
    for j in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
        newpoint = [point[0]+j[0],point[1]+j[1],point[2]+j[2]]
        if bounds[0][0]<=newpoint[0]<=bounds[1][0] and \
           bounds[0][1]<=newpoint[1]<=bounds[1][1] and \
           bounds[0][2]<=newpoint[2]<=bounds[1][2] and \
           newpoint not in air and newpoint not in queue \
           and newpoint not in cubes:
            queue.append(newpoint)
    air.append(point)

bl = [bounds[1][0]-bounds[0][0]+1,bounds[1][1]-bounds[0][1]+1,bounds[1][2]-bounds[0][2]+1]
p2 = getSurface(air) - 2*(bl[0]*bl[1]+bl[1]*bl[2]+bl[0]*bl[2])
print("Part 2:",p2)
