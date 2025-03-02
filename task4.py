X, Y, N = map(int, input().split())
total_kop = (X * 100 + Y) * N

rubles = total_kop // 100
kop = total_kop % 100

print(f"{rubles} руб. {kop} коп.")