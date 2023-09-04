import time


def decor1(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print("Время расчета:",(end-start), "s" )
        return result
    return wrapper


@decor1
def func(a):
    global b
    while a > 0:
        b = a/10
        a = a - 10
    return a, b

print(func(1000000000))