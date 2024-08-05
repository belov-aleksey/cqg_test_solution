# CQG Test Solution

## Описание
Решение тестового задания для CQG. Скрипт принимает два текстовых файла: конфигурационный файл с парами замен и файл с текстом, в котором будут произведены эти замены.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/belov-it/cqg_test_solution
    cd cqg_test_solution
    ```
2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Использование

1. Добавьте два текстовых файла в корневую директорию проекта:
    - `config.txt`: конфигурационный файл в формате `value1=value2`
    - `text.txt`: файл с текстом

2. Запуск скрипта:

    ```bash
    python3 solution/main.py config.txt text.txt
    ```

## Запуск тестов

1. Запуск тестов:

    ```bash
    pytest -v
    ```