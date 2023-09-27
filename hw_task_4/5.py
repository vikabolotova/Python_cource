import numpy as np


def matritsa(num):
    list_multipl = []

    if num > 2:
        for i in range(1, num + 1):
            if num % i == 0:
                list_multipl.append(i)
        print(list_multipl)

        if list_multipl == [num]:
            print('число нельзя разбить на множители без остатка ')

        matrices = []
        for i in range(2, len(list_multipl)):
            for j in range(i, len(list_multipl)):
                matrices.append((list_multipl[i - 1], list_multipl[j]))

        print("Возможные матрицы:")
        for matrix in matrices:
            print(matrix)

    else:
        print('Нельзя построить матрицу с такой размерностью ')


matritsa(1235)