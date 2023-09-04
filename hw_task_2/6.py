def decor1(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, int):
            raise TypeError("результат не соответствует типу integer ")
        return result
    return wrapper


@decor1
def test_1(a,b):
    return a*b

@decor1
def test_2(a,b):
    return a+b


print(test_1(5,6), test_2(10,5))
print(test_1(5,6), test_2("a","b"))


