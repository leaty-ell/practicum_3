seconds = int(input("Введите количество секунд: "))

hours = seconds // 3600
remaining_seconds = seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
    
print(f"Текущее время: {hours} ч. {minutes} мин. {seconds} сек.")