inpt = open("input.txt","r").read().strip()
grid = [[x for x in y] for y in inpt.split("\n")]
size = [len(grid[0]),len(grid)]
ht = "SabcdefghijklmnopqrstuvwxyzE"

def findCell(contents):
    for y in range(len(grid)):
        if contents in grid[y]:
            return [grid[y].index(contents),y]

def getCell(c):
    if 0<=c[0]<size[0] and 0<=c[1]<size[1]:
        return grid[c[1]][c[0]].replace("S","a").replace("E","z")
    return "a"

def pathfind(fr):
    checked = []
    queue = [fr+[[]]]
    lows = []
    
    while len(queue)>0:
        current = queue.pop(0)
        if current[:2] in checked:
            continue
        for direc in [[0,1],[1,0],[0,-1],[-1,0]]:
            new = [current[0]+direc[0],current[1]+direc[1]]
            lis = [ht.index(getCell(current)),ht.index(getCell(new))]
            if lis[1]<lis[0]-1:
                continue
            if getCell(new)=="a":
                lows += [new+[current[2]+[current[:2],new]]]
            if 0<=new[0]<size[0] and 0<=new[1]<size[1] and new not in checked:
                queue += [new+[current[2]+[current[:2]]]]
        checked += [current[:2]]
        if len(checked)%1000 == 0:
            print(len(checked),"/",size[0]*size[1])
    return lows

paths = pathfind(findCell("E"))
start = findCell("S")
path = [i for i in paths if i[:2]==start][0]
display = [y.copy() for y in grid]
for i in path[2]:
    display[i[1]][i[0]] = "#"
for y in display:
    print("".join(y))
print("Part 1:",len(path[2])-1)
print("Part 2:",min([len(i[2]) for i in paths])-1)
