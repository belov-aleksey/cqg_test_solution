# 1. Считываем конфиг файл. Строка файла value1=value2 это key=>value
# для словаря
# 2. Считываем построчно второй файл, бежим по строке и если символ в словаре
# с заменами - заменить его, счетчик замен +=1
# 3. Сортируем массив со счетчиками и меняем строки текстового файла также
import re
import argparse

# Объявление экземляра класса для аргументов командной строки
parser = argparse.ArgumentParser(description="Описание вашего скрипта")
parser.add_argument("filename1", type=str)
parser.add_argument("filename2", type=str)
args = parser.parse_args()


def parse_config_file(config_file_name):
    # Шаблон для конфигурационного файоа
    pattern = r"(\w)=(\w)"
    # Словарь для хренния замен
    replacements = {}
    with open(config_file_name, "r") as file:
        for line in file:
            match = re.match(pattern, line.strip("\n"))
            if match:
                replacements[match.group(1)] = match.group(2)
            else:
                print("Проверьте формат конфигурационного файла: value1=value2")
    return replacements


def parse_text_file(text_file_name, replacements):
    # Считывание строк с текстового файла
    with open(text_file_name, "r") as file:
        lines = file.readlines()
    # Список для хранения новых строк после замен
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
        new_lines.append(("".join(new_line).strip("\n"), count))
    # Сортировка по количеству замен в каждой строке
    sorted_pairs = sorted(new_lines, key=lambda x: x[1], reverse=True)
    return [pair[0] for pair in sorted_pairs]


replacements = parse_config_file(args.filename1)
sorted_lines = parse_text_file(args.filename2, replacements)


# Вывод в консоль
for line in sorted_lines:
    print(line)
