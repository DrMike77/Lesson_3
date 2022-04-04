def my_func(x,y,z):
    n = [x,y,z]
    n.sort()
    f = n[-1] + n[-2]
    return f
x, y, z = int(input("Введите число_1:")), int(input("Введите число_2:")), int(input("Введите число_3:"))
print(my_func(x,y,z))
