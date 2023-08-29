import random
rand_list = []
def random_list(n,a_1, a_2,elem):
    for i in range(n):
        rand_list.append(random.randint(a_1, a_2))
    print(rand_list)
    rand_list.append(elem)
    print(rand_list)


random_list(5,10,50,random.randint(1, 100000))

