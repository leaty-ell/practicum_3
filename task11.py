N = float(input("Введите количество градусов: "))

hours = int(N // 30)
minutes = int((N % 30) // 0.5)

print(f"{hours} {minutes}")