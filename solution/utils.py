import re


def parse_config_file(config_file_name):
    """Parse the configuration file and return a dictionary of replacements."""
    # Template for configuration file
    pattern = r"(\w)=(\w)"
    # Dictionary with replacements
    replacements = {}
    with open(config_file_name, "r") as file:
        for line in file:
            match = re.match(pattern, line.strip("\n"))
            if match and match.group(2):
                replacements[match.group(1)] = match.group(2)
            else:
                raise ValueError(
                    "Check the format of the configuration file: value1=value2"
                )
    return replacements


def parse_text_file(text_file_name, replacements):
    """
    Parse the text file and replace characters based on the replacements dictionary.

    Args:
        text_file_name (str): The name of the text file.
        replacements (dict): A dictionary where keys are characters to be replaced and values are replacement characters.

    Returns:
        list: A list of strings with characters replaced and sorted by the count of replacements in descending order.
    """
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
