class Rectangle:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def area(self):
        return print(self.a*self.b)

    def perimeter(self):
        return print((self.a+self.b)*2)
res = Rectangle(10,5)
res.area()
res.perimeter()