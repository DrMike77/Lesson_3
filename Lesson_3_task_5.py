s = 0
while True:
    numbers = input("Введите строку из чисел через пробел:").split()
    stop: bool = False

    for number in numbers:
        if number.isdigit():
            s += int(number)
        else:
            stop: bool = True
            break
    print(f"Общая сумма чисел = {s}")
    if stop: bool = True
    break