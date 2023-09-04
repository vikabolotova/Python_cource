def function_4(list_1, list_2):
    def func_4(list_1):
        return list_1 in list_2

    filtered_list = list(filter(func_4, list_1))
    return print(filtered_list)


list_1 = [1,2,3,4,5,6]
list_2 = [9,8,7,6,5,4]
function_4(list_1, list_2)

