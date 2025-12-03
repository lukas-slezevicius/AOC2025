with open("final.txt") as f:
    data = f.read()
    xs = [[int(x) for x in l] for l in data.strip().split("\n")]

s = 0
for x in xs:
    first_digit = x[-2]
    first_digit_idx = len(x) - 2
    for i in range(len(x) - 3, -1, -1):
        new_digit = x[i]
        if new_digit >= first_digit:
            first_digit = new_digit
            first_digit_idx = i

    second_digit = x[first_digit_idx + 1]
    for i in range(first_digit_idx + 1, len(x)):
        new_digit = x[i]
        if new_digit > second_digit:
            second_digit = new_digit

    s += first_digit*10 + second_digit

print(s)
