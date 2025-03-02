ATT = int(input("Введите количество попыток (ATT): "))
COMP = int(input("Введите количество завершенных пасов (COMP): "))
YDS = int(input("Введите количество ярдов (YDS): "))
TD = int(input("Введите количество тачдаунов (TD): "))
INT = int(input("Введите количество перехватов (INT): "))

a = ((COMP / ATT) - 0.3) * 5
b = ((YDS / ATT) - 3) * 0.25
c = (TD / ATT) * 20
d = 2.375 - ((INT / ATT) * 25)
    
rating = ((a + b + c + d) / 6) * 100
print(f"Рейтинг квотербека: {rating}")