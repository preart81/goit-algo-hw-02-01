"""Необхідно розробити функцію, яка приймає рядок як вхідний параметр, 
додає всі його символи до двосторонньої черги (deque з модуля collections в Python), 
а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 
Програма повинна правильно враховувати як рядки з парною, 
так і з непарною кількістю символів, 
а також бути нечутливою до регістру та пробілів."""

from collections import deque


def ispalindrome(text: str, debug=False) -> bool:
    """Перевірка чи є фраза паліндромом.

    Параметри:
    - text -- фраза для перевірки
    - debug -- False : повідомлення відладки

    Результат: bool
        True: якщо фраза є палндромом"""
    text = text.lower()
    text = "".join((filter(str.isalpha, text)))
    if debug:
        print(f"{text}, len={len(text)}")
        print(text[::-1])

    queue = deque(text)
    equal = True
    while equal and len(queue) >= 2:
        equal = queue.pop() == queue.popleft()
    return equal


if __name__ == "__main__":
    """Головний цикл"""

    class bcolors:
        RED = "\033[1;31m"
        BLUE = "\033[1;34m"
        CYAN = "\033[1;36m"
        GREEN = "\033[0;32m"
        RESET = "\033[0;0m"
        BOLD = "\033[;1m"
        REVERSE = "\033[;7m"

    test_texts = [
        "Я несу гусеня",
        "Козак з казок.",
        "Уже лисі ліси... Лежу.",
        "І що сало? Ласощі...",
        "І що салоо? Ласощі...",
        "Не паліндром",
        "Дід і дід",
        "Е, ти дурен, ерудите! ",
        "І розморозь зором зорі",
        "А результатів? Вітать лузера! ",
        "ау",
        "А",
    ]
    result = {
        True: bcolors.GREEN + "є паліндромом" + bcolors.RESET,
        False: bcolors.RED + "не є паліндромом" + bcolors.RESET,
    }
    for text in test_texts:
        check = ispalindrome(text)
        print(f"Текст '{text}' {result[check]} ")
