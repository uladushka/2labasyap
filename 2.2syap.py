import re
def foo(a):
    if isinstance(a, list):
        sum = 0
        for i in range(len(a)):
            if a[i] < 0:
                sum += a[i]
        a = set(a)
        a = list(a)
        print("""Из списка удалены все повторяющиеся элементы, новый список: """, a)
        print("""Сумма отрицательных чисел: """, sum)
    elif isinstance(a, set):
        a = str(a)
        word = re.findall('[a-zA-Z]+', a)
        print("Количество слов в наборе равно:", len(word))

    elif isinstance(a, int) or isinstance(a, float):
        if isinstance(a, float):
            print("Число непростое!:(\n")
            return
        if a == 1:
            print("Число", a, "простое!:)")
            return
        else:
            count = 1
            for i in range(2, a):
                if a % i != 0:
                    pass
                else:
                    print("Число", a, "непростое!:)")
                    return
            print("Число", a, "простое!:)")
    elif isinstance(a,str):                     #если строка
        llist=re.findall('[а-яА-Я]+', a)
        a = ''.join(llist)
        c1 = c2 = 0                         #
        for i in range(len(a)):
            if a[i] == 'е' or a[i] == 'а' or a[i] == 'у' or a[i] == 'и' or a[i] == 'о' or a[i] == 'я' or a[i] == 'ю' or a[i] == 'э':
                c1 += 1
            else:
                c2 += 1
        max = 0
        for i in range(1, len(llist)):
            if len(llist[i]) > len(llist[max]):
                max = i
        print("Кол-во гласных равно ", c1, "\nкол-во согласных равно ", c2, "\nсамое длинное слово это-", llist[max])


foo([1, 2, 4, -1, 5, -4, 4, -4])
foo("привет мама## !   $$ здравствуй")
foo(120)
foo(11)
foo({'Hello  hi!', 12, ' @$  Bye1', ' good 22   morning4        love+-', '+++', '  '})