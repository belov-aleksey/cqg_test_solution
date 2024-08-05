# CQG Test Solution

## Description
This is a solution for the CQG test task. The script accepts two text files: a configuration file with replacement pairs and a text file in which these replacements will be made.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/belov-it/cqg_test_solution
    cd cqg_test_solution
    ```
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Add two text files to the root directory of the project:
    - `config.txt`: Configuration file in the format `value1=value2`
    - `text.txt`: File with the text

2. Run the script:

    ```bash
    python3 solution/main.py config.txt text.txt
    ```

## Running Tests

1. Run the tests:

    ```bash
    pytest -v
    ```