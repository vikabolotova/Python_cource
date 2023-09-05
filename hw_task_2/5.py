def step(a, b):
    global d
    for i in range(a, b + 1):
        step(i + 1, b - i)
    if b == 0:
        d += 1


d = 0



N = 3

step(1, N)

print(d)