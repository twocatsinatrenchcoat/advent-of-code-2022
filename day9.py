inpt = open("input.txt","r").read().strip()
inst = [[i[0],int(i.split()[1])] for i in inpt.split("\n")]

def dist(c,d):
    e = c - d
    return max(abs(e.imag),abs(e.real))

def sgn(n):
    if n==0:
        return 0
    elif n<0:
        return -1
    return 1

def sim(rope,i):
    while dist(rope[i],rope[i+1])>1:
        diff = rope[i] - rope[i+1]
        rope[i+1] = (rope[i+1].real + sgn(diff.real)) + (rope[i+1].imag + sgn(diff.imag)) * 1j

moves = {"U": -1j, "D": 1j, "R": -1, "L": 1}

def simulateRope(knots):
    rope = [0 + 0j] * knots
    lasts = []
    for line in inst:
        for move in range(line[1]):
            rope[0] += moves[line[0]]
            for i in range(knots-1):
                sim(rope,i)
            lasts += [rope[-1]]
    return len(set(lasts))

print("Part 1:",simulateRope(2))
print("Part 2:",simulateRope(10))
