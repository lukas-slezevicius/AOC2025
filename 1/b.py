with open("final.txt") as f:
    moves = f.read().strip().split("\n")

pos = 50
count = 0
for move in moves:
    direction = 1 if move[0] == "R" else -1
    steps = int(move[1:])
    for _ in range(steps):
        pos = (pos + direction)%100
        if pos == 0:
            count += 1

print(count)
