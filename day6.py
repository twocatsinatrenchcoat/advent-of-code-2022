inpt = open("input.txt","r").read().strip()

def findNUnique(n,string):
    marker = 0
    while marker < len(string):
        valid = True
        attempt = string[marker:marker+n]
        for i in range(n-1):
            for j in range(i+1,n):
                if attempt[i]==attempt[j]:
                    valid = False
                    marker += i+1
                    break
            if not valid:
                break
        if valid:
            return marker

print("Part 1:",findNUnique(4,inpt)+4)
print("Part 2:",findNUnique(14,inpt)+14)
