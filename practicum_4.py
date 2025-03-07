#1
password = input("Введите пароль: ")
if password == "пароль":
    print("Проходи!")
else:
    print("Доступ запрещен!")


#2
first_word = input("Первое слово: ")
second_word = input("Второе слово: ")

if first_word == "Генрих" and second_word == "Герц":
    print("Верно")
else:
    print("Неверно")


#3
character_name = input("Имя персонажа: ")
character_name = character_name.lower()

if character_name == "джеймс бонд":
    print("Верно")
else:
    print("Неверно")


#4
answer = input("Вы поедете на бал? ")
answer = answer.lower()

if answer == "да" or answer == "нет":
    print("Неверно")
else:
    print("Верно")


#5
N = int(input("Количество рыб, пойманных первым рыбаком: "))
K = int(input("Количество рыб, пойманных вторым рыбаком: "))

if N < K:
    print(N)
elif K < N:
    print(K)
else:
    print(N)


#6
score = input("Введите счет: ")
team1, team2 = map(int, score.split(':'))

if team1 > team2:
    print("1")
elif team2 > team1:
    print("2")
else:
    print("0")


#7
scores = input("Введите рекорды: ")
score_list = list(map(int, scores.split()))

max_score = score_list[0]
for score in score_list:
    if score > max_score:
        max_score = score

print("Самый лучший результат:", max_score)


#8
name = input("Здравствуйте! Как Вас зовут? ")
print(f"Очень приятно, {name}! Меня зовут Марк.")

age = int(input("Сколько Вам лет? "))
mark_age = 80

if age < mark_age:
    print(f"Да, {name}, я старше Вас на {mark_age - age} лет.")
else:
    print(f"Да, {name}, Вы старше меня на {age - mark_age} лет.")

programming = input("Вам нравится программировать? ").lower()
if programming == "да":
    print("Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.")
else:
    print("Жаль. Я думал, Вы сможете написать интересную программу для меня.")


#9
fur = input("Собака короткошерстной породы? ")
if fur == "да":
    height = input("Рост собаки менее 50 см? ")
    if height == "да":
        tail_length = input("У собаки короткий хвост? ")
        if tail_length == "да":
            print("английский бульдог")
        else:
            ears_length = input("У собаки длинные уши? ")
            if ears_length == "да":
                print("гончая")
            else:
                body_length = input("У собаки короткое тело? ")
                if body_length == "да":
                    print("мопс")
                else:
                    print("чихуахуа")
    else:
        weight = input("Собака весит более 50 кг? ")
        if weight == "да":
            print("датский дог")
        else:
            print("фоксхаунд")
else:
    height = input("Рост собаки менее 50 см? ")
    if height == "да":
        character = input("У собаки доброжелательный характер? ")
        if character == "да":
            print("кокер-спаниэль")
        else:
            print("ирландский сеттер")
    else:
        height = input("У собаки рост менее 70 см? ")
        if height == "да":
            ears_length = input("У собаки длинные уши? ")
            if ears_length == "да":
                print("большой вандейский грифон")
            else:
                print("колли")
        else:
            color = input("Окрас рыжий с белыми отметинами? ")
            if color == "да":
                print("сенбернар")
            else:
                color = input("Белоснежный окрас? ")
                if color == "да":
                    print("ирландский волкодав")
                else:
                    print("ньюфаундленд")


#10
num_gears = int(input("Введите количество шестеренок: "))

if num_gears % 2 == 0:
    print("Механизм может вращаться.")
else:
    print("Механизм не может вращаться.")
