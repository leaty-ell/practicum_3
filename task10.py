X = int(input("Введите число X: "))
Y = int(input("Введите число Y: "))

result = int(X % Y == 0 or Y % X == 0)
print(result)