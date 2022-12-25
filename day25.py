inpt = open("input.txt","r").read().strip()
inpt = inpt.split("\n")

def fromSP(n):
    res = 0
    for i in n:
        res *= 5
        res += "=-012".index(i)-2
    return res

def toSP(n):
    res = ""
    while n>0:
        d = n%5
        if d>2:
            n+=5
        res = "012=-"[d] + res
        n = n//5
    return res

total = sum([fromSP(i) for i in inpt])
print("Part 1:",toSP(total))
