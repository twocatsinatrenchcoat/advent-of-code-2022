inpt = open("input.txt","r").read().strip()
nodes = [i.split(" ") for i in inpt.split("\n")]
nodes = {i[1]:{"rate":int(i[4][5:-1]),"conns":[j[:2] for j in i[9:]]} for i in nodes}

def explore(at):
    res = {}
    queue = [[at,0]]

    while len(queue)>0:
        current = queue.pop(0)
        if current[0] in res:
            continue
        for tunnel in nodes[current[0]]["conns"]:
            if tunnel not in res:
                queue += [[tunnel,current[1]+1]]
        res.update({current[0]:current[1]})
    return {i:res[i] for i in res if nodes[i]["rate"]>0}

best = 0
def dfs(opts,on,time,score,mt=30,p2=False):
    global best
    poss = score+(mt-time)*sum([nodes[j]["rate"] for i,j in enumerate(nodes) if (on & 2**i) == 0])
    if poss < best:
        return 0
    scores = []
    for i in opts:
        val = 2**(inds.index(i))
        if opts[i]+time<mt and (on & val) == 0:
            scores += [dfs(dists[i],on+val,time+opts[i]+1,score+(mt-time-opts[i]-1)*nodes[i]["rate"],mt,p2)]
    if p2 and time>15:
        scores += [dfs(start,on,0,score,26)]
    if scores == []:
        if score > best:
            best = score
            print(best)
        return score
    return max(scores)

dists = {i:explore(i) for i in nodes if nodes[i]["rate"]>0}
inds = [i for i in dists]
start = explore("AA")
print("Part 1:",dfs(start,0,0,0))
print("Part 2:",dfs(start,0,0,0,26,True)) # takes a while
