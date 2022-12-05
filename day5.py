inpt = open("input.txt","r").read()
grid, insts = inpt.split("\n\n")

insts = [i.split() for i in insts.strip().split("\n")]
insts = [[int(i[1]),int(i[3])-1,int(i[5])-1] for i in insts]

grid = [[i[j+1] for i in grid.split("\n")[:-1] if i[j+1]!=' '][::-1] for j in range(0,grid.index("\n"),4)]
gridb = [i.copy() for i in grid]

for i in insts:
    grid[i[2]] += grid[i[1]][:-i[0]-1:-1]
    grid[i[1]] = grid[i[1]][:-i[0]]
    
    gridb[i[2]] += gridb[i[1]][-i[0]:]
    gridb[i[1]] = gridb[i[1]][:-i[0]]

print("Part 1:","".join([i[-1] for i in grid]))
print("Part 2:","".join([i[-1] for i in gridb]))
