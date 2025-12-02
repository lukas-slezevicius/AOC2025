with open("final.txt") as f:
    moves = f.read().strip().split("\n")

pos = 50
count = 0
for move in moves:
    direction = move[0]
    steps = int(move[1:])
    if direction == "L":
        steps *= -1
    pos = (pos + steps)%100
    if pos == 0:
        count += 1

print(count)
