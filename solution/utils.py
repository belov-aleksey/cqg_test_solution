import re


def parse_config_file(config_file_name):
    # Template for configuration file
    pattern = r"(\w)=(\w)"
    # Dictionary with replacements
    replacements = {}
    with open(config_file_name, "r") as file:
        for line in file:
            match = re.match(pattern, line.strip("\n"))
            if match:
                replacements[match.group(1)] = match.group(2)
            else:
                print("Check the format of the configuration file: value1=value2")
    return replacements


def parse_text_file(text_file_name, replacements):
    with open(text_file_name, "r") as file:
        lines = file.readlines()
    # List with pairs (new lines, count of replacements)
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
    # Sort by count of replacements in each line
    sorted_pairs = sorted(new_lines, key=lambda x: x[1], reverse=True)
    return [pair[0] for pair in sorted_pairs]
