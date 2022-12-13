inpt = open("input.txt","r").read().strip()
pairs = [[eval(j) for j in i.split("\n")] for i in inpt.split("\n\n")]

def compare(a,b):
    if type(a) == int and type(b) == int:
        if a<b:
            return True
        elif a>b:
            return False
        return 0
    elif type(a) == list and type(b) == list:
        for s in range(min(len(a),len(b))):
            res = compare(a[s],b[s])
            if type(res) == bool:
                return res
        if len(a)<len(b):
            return True
        elif len(a)>len(b):
            return False
        return 0
    elif type(a) == list and type(b) == int:
        return compare(a,[b])
    elif type(a) == int and type(b) == list:
        return compare([a],b)

def sort(array):
    newarr = [array[0]]
    for i in array[1:]:
        for j,k in enumerate(newarr):
            if compare(i,k):
                newarr.insert(j,i)
                break
        newarr.append(i)
    return(newarr)

n=0
for i,j in enumerate(pairs):
    if compare(j[0],j[1]):
        n += i + 1

print("Part 1:",n)

packets = [[[2]],[[6]]]
for i in pairs:
    packets += i

packets = sort(packets)

print("Part 2:",(packets.index([[2]])+1)*(packets.index([[6]])+1))
