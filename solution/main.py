import argparse
from utils import parse_config_file, parse_text_file


def main():
    # Declaring a class instance for command line arguments
    parser = argparse.ArgumentParser(description="Описание вашего скрипта")
    parser.add_argument("filename1", type=str)
    parser.add_argument("filename2", type=str)
    args = parser.parse_args()

    replacements = parse_config_file(args.filename1)
    sorted_lines = parse_text_file(args.filename2, replacements)

    for line in sorted_lines:
        print(line)


if __name__ == "__main__":
    main()
