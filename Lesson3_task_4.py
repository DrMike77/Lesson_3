def my_func(x,y):
    return x ** y
def my_func2(x,y):
    f2 = x
    if y > 0:
       for i in range(1, y):
         f2 *= x
    else:
       for i in range(1,y, -1):
                f2 /= x
    return f2
a, b = float(input("Введите число_1")), int(input("Введите число_2"))
print((my_func(a, b)))
print(my_func2(a, b))