bitcoin_price = input("Введите стоимость биткоина в рублях: ")

if len(bitcoin_price) < 3:
    print("Стоимость должна содержать как минимум три цифры.")
else:
    print(f"Цифра на третьей позиции справа: {bitcoin_price[-3]}")