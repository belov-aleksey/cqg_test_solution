# 1. Считываем конфиг файл. Строка файла value1=value2 это key=>value
# для словаря
# 2. Считываем построчно второй файл, бежим по строке и если символ в словаре
# с заменами - заменить его, счетчик замен +=1
# 3. Сортируем массив со счетчиками и меняем строки текстового файла также

import argparse
from utils import parse_config_file, parse_text_file

def main():
    # Объявление экземляра класса для аргументов командной строки
    parser = argparse.ArgumentParser(description="Описание вашего скрипта")
    parser.add_argument("filename1", type=str)
    parser.add_argument("filename2", type=str)
    args = parser.parse_args()

    replacements = parse_config_file(args.filename1)
    sorted_lines = parse_text_file(args.filename2, replacements)

    # Вывод в консоль
    for line in sorted_lines:
        print(line)


if __name__ == "__main__":
    main()