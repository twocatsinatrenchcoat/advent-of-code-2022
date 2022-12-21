inpt = open("input.txt","r").read().strip()
raw = [i.split(": ") for i in inpt.split("\n")]
raw = {i[0]:i[1] for i in raw}

def calc(name):
    if raw[name].isdigit():
        val = int(raw[name])
    else:
        f = raw[name].split(" ")
        v1 = calc(f[0])
        v2 = calc(f[2])
        val = eval(str(v1)+f[1]+str(v2))
    return val

def pathfind(start,end):
    if start == end:
        return [start]
    if raw[start].isdigit():
        return 0
    edges = raw[start].split(" ")[::2]
    for i in edges:
        j = pathfind(i,end)
        if j != 0:
            return [start]+j
    return 0

def reversecalc(name,mbet):
    if name == "humn":
        return mbet
    #print(name,"=",raw[name],"=",mbet)
    args = raw[name].split(" ")
    op = args.pop(1)
    inv = (args[1] in aff)
    if op == "+":
        if inv:
            return reversecalc(args[1],mbet-calc(args[0])) # a + b = c -> b = c - a
        return reversecalc(args[0],mbet-calc(args[1]))     # a + b = c -> a = c - b
    elif op == "-":
        if inv:
            return reversecalc(args[1],calc(args[0])-mbet) # a - b = c -> b = a - c
        return reversecalc(args[0],calc(args[1])+mbet)     # a - b = c -> a = b + c
    elif op == "*":
        if inv:
            return reversecalc(args[1],mbet/calc(args[0])) # a * b = c -> b = c / a
        return reversecalc(args[0],mbet/calc(args[1]))     # a * b = c -> a = c / b
    else: #op == "/"
        if inv:
            return reversecalc(args[1],calc(args[0])/mbet) # a / b = c -> b = a / c
        return reversecalc(args[0],mbet*calc(args[1]))     # a / b = c -> a = b * c

print("Part 1:",int(calc("root")))

aff = pathfind("root","humn")
goal = raw["root"].split(" ")[::2]
if goal[0] in aff:
    goal = goal[1]
else:
    goal = goal[0]
goal = calc(goal)

print("Part 2:",int(reversecalc("root",2*goal)))
