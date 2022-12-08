inpt = open("input.txt","r").read().strip()
grid = [[x for x in y] for y in inpt.split()]
scores = []

def raycast(c,dc):
    ht = int(grid[int(c.imag)][int(c.real)])
    dist = 0
    while -1<(c+dc).imag<len(grid) and -1<(c+dc).real<len(grid[0]):
        c += dc
        dist += 1
        if int(grid[int(c.imag)][int(c.real)])>=ht:
            return [False,dist]
    return [True,dist]

vis = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        visible = False
        c = x + y * 1j
        dc = 1j
        score = 1
        for i in range(4):
            thisdir = raycast(c,dc**i)
            score *= thisdir[1]
            if thisdir[0]:
                visible = True
        if visible:
            vis += 1
        scores += [score]

print("Part 1:",vis)
print("Part 2:",max(scores))
