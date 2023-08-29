import random

def list_1(list):
    a = 0
    for number in list:
        if number < 0:
            a = a+1
    print(a)



list = []
for i in range(5):
    list.append(random.randint(-100, 100))
print(list)

list_1(list)