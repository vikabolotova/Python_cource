def stup(a, b):
    global d
    print("заново")
    for i in range(a, b + 1):
        stup(i + 1, b - i)
        print(a,b)
    if b == 0:
        d += 1
        print(d)

d = 0



N = 3

stup(1, N)

print(d)