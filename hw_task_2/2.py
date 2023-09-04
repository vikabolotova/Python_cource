
def function(a,spisok):
    return list(filter(lambda x: x % a ==0, spisok))

print(function(2,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))