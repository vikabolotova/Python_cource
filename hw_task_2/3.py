def func_3(*args):
    return str(args)

tuple = func_3(1,3,5,7,"vdv")
print(tuple)
print(type(tuple[2]))