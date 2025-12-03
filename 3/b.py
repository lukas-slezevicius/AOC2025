with open("final.txt") as f:
    data = f.read()
    xs = [[int(x) for x in l] for l in data.strip().split("\n")]

def find_max(nums, from_idx, to_idx):
    digit = nums[to_idx]
    digit_idx = to_idx
    for i in range(to_idx, from_idx - 1, -1):
        new_digit = nums[i]
        if new_digit >= digit:
            digit = new_digit
            digit_idx = i
    return digit, digit_idx

s = 0
for x in xs:
    last_digit_idx = -1
    nums_left = 12
    while nums_left > 0:
        digit, last_digit_idx = find_max(x, last_digit_idx + 1, len(x) - nums_left)
        nums_left -= 1
        s += digit * 10**nums_left
print(s)
