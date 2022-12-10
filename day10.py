inpt = open("input.txt","r").read().strip()
inst = inpt.replace("addx","(busy)\naddx").split("\n")

grid = []
x1 = 1
for i, j in enumerate(inst):
    if j.startswith("addx"):
        x1 += int(j.split()[1])
    grid += [x1]

sum1 = 0
for i, j in enumerate(grid[18::40]):
    sum1 += ((2*i)+1)*j*20

print("Part 1:",sum1)
print("Part 2:")

readout = ""
for y in range(6):
    for x in range(40):
        if x-2<grid[x+(y*40)-1]<x+2:
            readout += "##"
        else:
            readout += ".."
    readout += "\n"

print(readout)
