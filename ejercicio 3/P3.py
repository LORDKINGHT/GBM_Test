def min_jump(x):
    cur = 0
    jump = 1
    while cur < x:
        cur += jump
        jump += 1
    return jump  if cur == x + 1 else jump - 1

first_case = [1, 2, 3, 4, 5]
for x in first_case:
    print(min_jump(x))