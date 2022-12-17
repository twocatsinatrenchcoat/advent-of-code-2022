inpt = open("input.txt","r").read().strip()
jets = [[2,0.5]["<>".index(i)] for i in inpt]
tiles = [[30],[8,28,8],[28,4,4],[16,16,16,16],[24,24]]
board = []

def dropTile():
    global board
    board += [0,0,0,0,0,0,0]
    ht = len(board)-4
    tile = tiles.pop(0)
    tiles.append(tile)
    while True:
        mult = jets.pop(0)
        jets.append(mult)
        canMoveAcross = sum([1 for i,j in enumerate(tile) if ((j*mult > 127 or (j*mult)%1>0) or (int(j*mult) & board[ht+i])>0)])==0
        if canMoveAcross:
            tile = [int(i*mult) for i in tile]
        canMoveDown = (sum([j & board[ht+i-1] for i,j in enumerate(tile)])==0) and ht>0
        if not canMoveDown:
            break
        ht -= 1
    for i,j in enumerate(tile):
        board[ht+i] += j
    while board[-1] == 0:
        board.pop(-1)

def draw():
    global board
    for i in board[::-1]:
        print("|"+bin(i)[2:].rjust(7,"0").replace("0",".").replace("1","#")+"|")
    print("-"*9+"\n")

for i in range(2022):
    dropTile()
print("Part 1:",len(board))

search = board[-20:]
sh = len(board)
p = 1
dropTile()
while board[-20:] != search:
    dropTile()
    p += 1
ch = len(board)-sh
cyclesleft = 1000000000000-2022-p
timeskip = (cyclesleft//p)*ch
extras = cyclesleft%p
for i in range(extras):
    dropTile()
p2 = timeskip + len(board)
print("Part 2:",p2)
