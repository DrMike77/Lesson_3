def pers_info(**kwargs):
    return f"{kwargs['name']} {kwargs['sur_name']} {kwargs['year']}, {kwargs['city']}, {kwargs['phone']}, {kwargs['email']}"
name1 = input("Введите Имя:")
sur_name1 = input("Введите Фамилию:")
year1 = int(input("Введите Год рождения:"))
city1 = input("Введите Город:")
email1 = input("Введите Email:")
phone1 = input("Введите Номер телефона:")
print(pers_info(name=name1, sur_name=sur_name1, city=city1, year=year1, email=email1, phone=phone1))