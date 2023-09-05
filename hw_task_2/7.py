import random

def decorator(func):
    def wrapper(*args, **kwargs):
        retries = 0
        while retries < 3:
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Исключение {e} при вызове func_1, повторная попытка")
                retries += 1
        raise Exception(f"Не удалось выполнить func_2 после 3 попыток")
    return wrapper



@decorator
def func_1(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

@decorator
def func_2():
    if random.random() < 0.5:
        raise Exception("Ошибка при получении данных")
    return "Данные успешно получены"




try:
    result = func_1(10, 5)
    print("Результат func_1:", result)
except Exception as e:
    print("Ошибка:", e)

try:
    data = func_2()
    print("Результат func_2:", data)
except Exception as e:
    print("Ошибка:", e)
