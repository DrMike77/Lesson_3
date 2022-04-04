def my_div(arg_1 = 1, arg_2 = 2):
    if arg_2 != 0:
        return arg_1 / arg_2
    else: print("Ошибка - попытка деления на 0, операция отменена")
x = [float(input("Введите первое число")), float(input("Введите второе число"))]
print(my_div(x[0], x[1]))

