inpt = open("input.txt","r").read().strip()

def mix():
    global l
    global n
    for i in range(len(l)):
        move = l[i]
        source = n.index(move)
        goal = (source + move[0]) % (len(l)-1)
        n.insert(goal,n.pop(source))

def output(part):
    z = inpt.split("\n").index("0")
    ind = n.index([0,z])
    ind = [(ind+1000)%len(l),(ind+2000)%len(l),(ind+3000)%len(l)]
    print("Part "+str(part)+":",sum([n[i][0] for i in ind]))

l = [[int(j),i] for i,j in enumerate(inpt.split("\n"))]
n = l.copy()
mix()
output(1)

l = [[int(j)*811589153,i] for i,j in enumerate(inpt.split("\n"))]
n = l.copy()
for i in range(10):
    mix()
output(2)
