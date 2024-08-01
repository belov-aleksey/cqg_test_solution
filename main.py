# 1. Считываем конфиг файл. Строка файла value1=value2 это key=>value 
# для словаря
# 2. Считываем построчно второй файл, бежим по строке и если символ в словаре 
# с заменами - заменить его, счетчик замен +=1 
# 3. Сортируем массив со счетчиками и меняем строки текстового файла также
import re
import argparse

# Объявление экземляра класса для аргументов командной строки
parser = argparse.ArgumentParser(description="Описание вашего скрипта")
parser.add_argument('filename1', type=str)
parser.add_argument('filename2', type=str)
args = parser.parse_args()


# Шаблон для конфигурационного файоа
pattern = r"(\w)=(\w)"
# Словарь для хренния замен
replacements = {}
with open(f'{args.filename1}', 'r') as file:
    for line in file:
        match = re.match(pattern, line.strip('\n'))
        if match:
            replacements[match.group(1)] = match.group(2)
        else:
            print("Проверьте формат конфигурационного файла: value1=value2")

# Считывание строк с текстового файла
with open(f'{args.filename2}', 'r') as file:
    lines = file.readlines()
# Список для хранения новых стрко после замен
new_lines = []
for line in lines:
    count = 0
    new_line = []
    for char in line:
        if char in replacements:
            new_line.append(replacements[char])
            count += 1
        else:
            new_line.append(char)
    new_lines.append(("".join(new_line).strip('\n'), count))

# Сортировка по количвеству замен в каждой строке
sorted_pairs = sorted(new_lines, key = lambda x: x[1], reverse=True)
sorted_lines = [pair[0] for pair in sorted_pairs]

# Вывод в консоль
for line in sorted_lines:
    print(line)


