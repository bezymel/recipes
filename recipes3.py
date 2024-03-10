# Чтение содержимого файлов
with open('2.txt', 'r') as file_2:
    content_2 = file_2.read().strip()

with open('1.txt', 'r') as file_1:
    content_1 = file_1.readlines()

with open('3.txt', 'r') as file_3:
    content_3 = file_3.readlines()

# Обновление времени в файле 2.txt
time_str = content_1[0].split()[4]  # извлечение времени из первой строки файла 1.txt
time_str = time_str.replace('шестнадцать', 'тридцать')  # замена времени
content_2 = f"{content_2.split()[0]} {time_str}"  # обновление времени в файле 2.txt

# Запись обновленных данных
with open('2.txt', 'w') as file_2:
    file_2.write(content_2)

with open('1.txt', 'w') as file_1:
    file_1.writelines(content_1)

with open('3.txt', 'w') as file_3:
    file_3.writelines(content_3)