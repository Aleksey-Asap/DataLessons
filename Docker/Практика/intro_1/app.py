from datetime import datetime

# Получаем текущую дату и время
current_time = datetime.now()

# Преобразуем объект datetime в строку с помощью метода strftime
formatted_time = current_time.strftime("%H:%M:%S")

print("Текущее время:", formatted_time)