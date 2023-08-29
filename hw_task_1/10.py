lst = [2, 4, 5, 8, 9, 13]

#for number in range(len(lst)):
#    lst[number] *= number
#    print(lst)



for i, value in enumerate(lst):
    lst[i] *= i
print(lst)