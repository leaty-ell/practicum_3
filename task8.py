import math

a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

if a + b > c and a + c > b and b + c > a:
    # используем т. косинусов: a**2 = b**2 + c**2 - 2*b*c * cos(A)
    alpha = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    beta = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    gamma = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
    
    print(f"Угол α: {alpha}")
    print(f"Угол β: {beta}")
    print(f"Угол γ: {gamma}")
else:
    print("Треугольник с такими сторонами не существует.")
