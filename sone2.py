##2 Экранированные последовательности

#S="s\np\ta\nbbb"
#count=0
#while True:
#    if count>=len(S):
#        break
#    count+=1
#print("Sümbolite arv reas :", count)
   
#   #3 Повторение строки
#S1="Rida kordamine"
#count=0
#while True:
#    if count<3:
#        print(S1*3)
#        count+=1
#    else:
#        break

#   #4 Длина строки
#S="Joone pikkus"
#pikkus=0
#while True:
#    if pikkus<len(S):
#        pikkus+=1
#    else:
#        break
#print("Joone pikkus:", pikkus)

spisok=[] #пустой список
numbers=[1,2,3,4,5]
abc=['Abc', 'B', 'C']
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1-Добавить букву в список")
    valik=int(input())
    if valik==1:
        a = input("Введи букву")
        slovo_list.append(a)
        print(f"Добавили {a} новый список", slovo_list)
    elif valik==2:
            slovo_list.extend(abc)
            print(slovo_list)
    elif valik==3:
        a = input("Введи букву которую хочешь добавить")
        i = int(input("Введи номер позиции, куда хочешь добавить букву"))
        slovo_list.insert(i - 1,a)
    elif valik==4:
        example_code="""
        # Пример использования метода isspace()
        s = "  " # пример строки, состоящей только из пробельных символов
        result = s.isspace()
        print(result) # Выведет True, если строка состоит только из символов
        """
        print("Пример использования метода isspace():")
        s = input("Что вы хотите вывести?")
        result = s.inspace()
        print(example_code)
        print(result)
    elif valik==5:
        a = input("Выведи букву, которую хочешь удалить")
        n = slovo_list.count(a)
        if n > 0:
            for i in range(n):
                slovo_list.remove(a)
        else:
            print(f"Буквы {a} нет в списке")
            print(slovo_list)
    elif valik == 6:
        slovo_list.clear()
        print("Список очищен")
    elif valik == 7:
        print("Пример использования метода s.swapcase():")
        s=input("Что вы хотите ввести?")
        result=s.swapcase()
        print(result)
    elif valik == 8:
        print("Пример использования метода .replace()")
        s = "Я намерен жить вечно или умереть, пытаясь это сделать"
        s = s.replace("Жить", "умереть")
        print(s)
    elif valik == 9:
        a=input("Введите слово или набор букв с маленькой и большой буквы\n")
        i=a.title()
        print(1)
    elif valik == 10:
        S="Programmeerimine Marina"
        print(S)
        K = input("Что вы хотите найти?")
        index = S.find(K)
        print(f"Esimese rea indeks {K}", index)
    elif valik == 11:
        print("Выход")
        break
    else:
        print("Выбрана некорректная операция. Попробуйте снова.")

try:
    while True:
        print("Kirjutage Tekst ja  me kontrolime kas teie tekst sisaldab numbrid, tähti, numbreid ja tähti, kas rida algab")
        
        a=input("Kirjutage tekst: ")
        
        a1 =[]

        if any(char.isdigit() for char in a):
            a1.append("Number")
        if any(char.isalpha() for char in a):
            a1.append("Täht")
        if any(char.isalnum() for char in a):
            a1.append("Numbrid ja kirjad")
        if any(char.isspace() for char in a):
            a1.append("Tühik")
        if any(char.istitle() for char in a):
            a1.append("Algustähega")
        if not a1:
            print("Midagi pole")
        else:
            print("Siin on:", a1)
except :
    print("Vale andmetüüp")



while True:
    if input("Sisestage string (või 'quit', et lõpetada): ").lower() == 'quit':
        print("Programmi lõpetamine...")
        break
    separator = input("Sisestage eraldaja: ")
    input_str = input("Sisestage string: ")
    parts = input_str.rsplit(separator, 1)
    if len(parts) == 1:
        result = ('', '', parts[0])
    else:
        result = (parts[0], separator, parts[1])
    print("Funktsiooni rpartition tulemus:"), result



