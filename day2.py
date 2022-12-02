inpt = open("input.txt","r").read().strip()
moves = [i.split() for i in inpt.split("\n")]

score1 = 0
score2 = 0

for i in moves:
    j = ["ABC".index(i[0]),"XYZ".index(i[1])]

    score1 += j[1]+1 + (4-(j[0]-j[1]))%3*3
    score2 += j[1]*3 + (j[0]+j[1]-1)%3+1

print("Part 1:",score1)
print("Part 2:",score2)
