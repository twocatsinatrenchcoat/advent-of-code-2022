inpt = open("input.txt","r").read().strip()

part1 = [sum([int(j) for j in i.split("\n")]) for i in inpt.split("\n\n")]
print(max(part1))

part2 = sorted(part1)
print(sum(part2[-3:]))
