inpt = open("input.txt","r").read().strip()
width = inpt.index("\n")
elves = [(i%width+(i//width)*1j) for i,j in enumerate(inpt.replace("\n","")) if j=="#"]

direx = [-1j,1j,-1,1]

i = 0
while True:
    if i%5==0:
        print(i)
    tgts = []
    for elf in elves:
        moves = False
        wantstomove = False
        goal = elf
        for d in direx:
            if elf + d not in elves and elf + d + (d*1j) not in elves and elf + d + (d*-1j) not in elves:
                if not moves:
                    goal = elf+d
                    moves = True
            else:
                wantstomove = True
        if not wantstomove:
            goal = elf
        tgts.append(goal)
    if tgts == elves:
        print("Part 2:",i+1)
        break
    for j,k in enumerate(tgts):
        if tgts.count(k)==1:
            elves[j] = k
    direx.append(direx.pop(0))
    if i==9:
        bwdth = [int(i.real) for i in elves]
        bhght = [int(i.imag) for i in elves]
        print("Part 1:",(max(bwdth)-min(bwdth)+1)*(max(bhght)-min(bhght)+1)-len(elves))
    i += 1
