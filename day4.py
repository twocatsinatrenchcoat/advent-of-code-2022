inpt = open("input.txt","r").read().strip()
inpt = [[[int(k) for k in j.split("-")] for j in i.split(",")] for i in inpt.split("\n")]

def fulloverlap(a,b):
    return (a[0]>=b[0] and a[1]<=b[1])

def partoverlap(a,b):
    return (b[0]<=a[0]<=b[1] or b[0]<=a[1]<=b[1])

fullols = 0
partols = 0
for i in inpt:
    if fulloverlap(i[0],i[1]) or fulloverlap(i[1],i[0]):
        fullols += 1
    if partoverlap(i[0],i[1]) or partoverlap(i[1],i[0]):
        partols += 1

print("Part 1:",fullols)
print("Part 2:",partols)
