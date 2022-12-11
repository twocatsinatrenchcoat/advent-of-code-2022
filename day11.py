import math
inpt = open("input.txt","r").read().strip()
inpt = [i.split("\n")[1:] for i in inpt.split("\n\n")]

def pF(n):
    l=[]
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            l.append(i)
            l+=pF(n//i)
            break
    if len(l)==0:
        return [n]
    return l

def union(a,b):
    c = a
    for i in b:
        if c.count(i)<b.count(i):
            c += [i]
    return c

def prod(l):
    res = 1
    for i in l:
        res *= i
    return res

def sim(rounds,confident):
    global inpt
    monkeys = [[[int(j) for j in i[0][18:].split(", ")],i[1][19:],int(i[2][21:]),int(i[3][29:]),int(i[4][30:]),0] for i in inpt]
    divisors = []
    for i in monkeys:
        divisors = union(divisors,pF(i[2]))
    lcm = prod(divisors)
    for i in range(rounds):
        for j in monkeys:
            while len(j[0])>0:
                old = j[0].pop(0)
                new = eval(j[1])
                if confident:
                    new = math.floor(new/3)
                else:
                    new = new%lcm
                if new%j[2]==0:
                    monkeys[j[3]][0] += [new]
                else:
                    monkeys[j[4]][0] += [new]
                j[5] += 1
        ## this snippet partially for debugging, partially for getting less impatient with part 2
        # if i%1000==0:
        #     print(i,[x[5] for x in monkeys])
    return monkeys

activity1 = sorted([x[5] for x in sim(20,True)])
print("Part 1:",activity1[-1]*activity1[-2])
activity2 = sorted([x[5] for x in sim(10000,False)])
print("Part 2:",activity2[-1]*activity2[-2])
