with open("final.txt") as f:
    data = [[int(n) for n in x.split("-")] for x in f.read().strip().split(",")]

wrong_nums = set()
n = 1
max_n = max(x for y in data for x in y)
while True:
    times = 2
    while True:
        x = int(str(n)*times)
        if x > max_n:
            break
        for a, b in data:
            if x >= a and x <= b:
                wrong_nums.add(x)
        times += 1
    x = int(str(n)*2)
    if x > max_n:
        break
    n += 1

print(sum(wrong_nums))
