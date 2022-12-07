inpt = open("input.txt","r").read().strip()
code = inpt.split("\n")

path = "C:"
files = {}
sizes = {}

line = 0
while line < len(code):
    if code[line][0] == "$":
        if code[line][2:4] == "ls":
            line += 1
            continue
        elif code[line].split()[2] == "..":
            path = path[:-path[::-1].index("/",1)]
        else:
            path += code[line].split()[2]+"/"
    else:
        if path not in files:
            files.update({path:[]})
        files[path] += [code[line]]
    line += 1

def getSize(path):
    size = 0
    for file in files[path]:
        if file.split()[0] == "dir":
            size += getSize(path+file.split()[1]+"/")
        else:
            size += int(file.split()[0])
    sizes[path] = size
    return size

currentsize = getSize("C://") # screw the principle of least surprise, this is just too nice a piece of code

print("Part 1:",sum([sizes[i] for i in sizes if sizes[i]<100000]))
print("Part 2:",min([sizes[i] for i in sizes if currentsize-sizes[i]<40000000]))
