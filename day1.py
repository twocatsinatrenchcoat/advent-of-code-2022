inpt = open("input.txt","r").read().strip()

part1 = [sum([int(j) for j in i.split("\n")]) for i in inpt.split("\n\n")]
print("Part 1:",max(part1))

part2 = sorted(part1)
print("Part 2:",sum(part2[-3:]))
