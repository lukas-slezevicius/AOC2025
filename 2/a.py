with open("final.txt") as f:
    data = [[int(n) for n in x.split("-")] for x in f.read().strip().split(",")]

wrong_nums = []
for a, b in data:
    n = 1
    while True:
        x = int(str(n)*2)
        if x >= a and x <= b:
            wrong_nums.append(x)
        if x > b:
            break
        n += 1
print(sum(wrong_nums))
