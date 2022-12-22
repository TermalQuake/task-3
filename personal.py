import tabulate # Импорт табурета


# Страница со списоком людей
def spisok():
    print(" Список всех пассажиров авиарейса:")
    from tabulate import tabulate
    #data = []
    with open('list.txt','r', encoding="utf-8") as f: #открытие файла и добавление формата
        data = [line.split(',') for line in f]
        data.sort(key = lambda x : x[3], reverse=False)
        for line in f:
            data.append(list(map(str.strip, line.split(',')))) #сама табуретка
    print(tabulate(data, tablefmt='grid', headers=('Фамилия', 'Номер удостоверения личности', 'Место', 'Вес Багажа'))) #формат и что будет написано
    avg()

#Нет багажа
def net():
    print("\n" * 5)
    print ("Список пассажиров у которых нет багажа:")
    from tabulate import tabulate
    data = []
    with open('list.txt',encoding="utf-8") as f:
        for line in f:
            if '0' in line.split():
                data.append(list(map(str.strip, line.split(',')))) #сама табуретка
    print(tabulate(data, tablefmt='grid', headers=('Фамилия', 'Номер удостоверения личности', 'Место', 'Вес Багажа'))) #формат и что будет написано
    minavg()

#Ниже среднего веса
def minavg():
    print("\n" * 5)
    from tabulate import tabulate
    print("Список пассажиров, у которых вес багажа ниже среднего:")
    data = []
    with open('list.txt','r', encoding="utf-8") as f:
        total = 0
        count = 0
        for line in f:
            field1, field2, field3, field4 = line.split(',')
            total += int(field4)
            count += 1
            result = round(total / count)
            a = int(result)
            b = int(field4)
            if a>=b:
                data.append(list(map(str.strip, line.split(','))))
    print(tabulate(data, tablefmt='grid', headers=('Фамилия', 'Номер удостоверения личности', 'Место', 'Вес Багажа')))
    maxavg()
#Выше среднего
def maxavg():
    print("\n" * 5)
    from tabulate import tabulate
    print(" Список пассажиров, у которых вес багажа выше среднего:")
    data = []
    with open('list.txt','r', encoding="utf-8") as f:
        total = 0
        count = 0
        for line in f:
            field1, field2, field3, field4 = line.split(',')
            total += int(field4)
            count += 1
            result = round(total / count)
            a = int(result)
            b = int(field4)
            if a<=b:
                data.append(list(map(str.strip, line.split(','))))
    print(tabulate(data, tablefmt='grid', headers=('Фамилия', 'Номер удостоверения личности', 'Место', 'Вес Багажа')))

#Считает среднее значение
def avg():
    with open('list.txt',encoding="utf-8") as f:
        total = 0
        count = 0
        for line in f:
            field1, field2, field3, field4 = line.split(',')
            total += int(field4)
            count += 1
    result = round(total / count)
    print("Средний вес багажа всех пассажиров:")
    print(result)
    net()

#Добавить  чела
#Name - фамилия, Nomer - Номер, Pos - Место, Heft - Вес, kg
def add(Name=None, Nomer=None, Pos=None, Exp=None):
    Name = input("Введи фамилию пассажира:")
    Nomer = input("Введи номер удостоверения пассажира:")
    Pos = input("Введи посадочное место пассажира:")
    Heft = input("Введи вес багажа пассажира:")
    list = open("list.txt", "a", encoding="utf-8")                       # Открывает список  и ставит кадировку
    list.write(Name+", "+str(Nomer)+ ", "+str(Pos)+", "+str(Heft)+"\n")     #записывает  в файл
    print("Сотрудник добавлен!")
    list.close()                              #сохраняет и закрывает
    home()                                # кидает обратно

#страница удаления
def remove(Name1=None, Nomer2=None):
    spisok()
    Name1 = input ("Напиши фамилию пассажира, которого надо удалить:")
    Nomer2 = input ("Напиши посадочное место пассажира:")
    fn = 'list.txt'   #открывает лист
    f = open(fn, encoding="utf-8")
    output = []
    for line in f:
        if not (Name1 and Nomer2) in line:
            output.append(line)
    f.close()
    f = open(fn, 'w', encoding="utf-8")
    f.writelines(output)
    f.close()
    print('''Теперь он не пассажир. Возвращение на главную страницу...
    ---
    
    ---''')
    home()


def home(): # Главная страница
    print('''Выберите пункт меню:
    1. Показать список пассажиров
    2. Добавить пассажира
    3. Удалить пассажира''')
    user_input = input()
    if user_input == '1':
        spisok()
    elif user_input == '2':
        add()
    elif user_input == '3':
        remove()
    else:
        print("Ты что-то не так написал")
home()
