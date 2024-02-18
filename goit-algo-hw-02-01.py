"""Програма, яка імітує приймання й обробку заявок: 
програма має автоматично генерувати нові заявки 
(ідентифіковані унікальним номером або іншими даними), 
додавати їх до черги, а потім послідовно видаляти з черги для
"обробки", імітуючи таким чином роботу сервісного центру."""

import time
from pprint import pprint
from queue import (
    PriorityQueue,
)  # Замість звичайного Queue використаємо пріоритезовану чергу
from random import random, choice
from colorama import Fore, Style
import keyboard

# Пріоритети заявок

prioritys = {
    0: "High",
    1: "Normal",
}


# Функція generate_request():
def generate_request(queue: PriorityQueue, id_rqst: int):
    """Генерація заявки для обробки

    Параметри:
    - queue -- черга
    - id_rqst -- ID попереднього запиту"""
    # Створити нову заявку
    id_rqst += 1
    priority_num, priority_txt = choice(list(prioritys.items()))
    request = f"Заявка #{id_rqst:3}"

    # Додати заявку до черги
    queue.put((priority_num, request))
    print(
        f"{Fore.YELLOW}Додано в чергу: {request} пріоритет {priority_txt}{Style.RESET_ALL}"
    )
    return id_rqst  # повертаємо ID заявки


# Функція process_request():
def process_request(queue):
    """Обробка заявки

    Параметри:
    - queue -- черга"""
    # global queue, id_rqst
    # Якщо черга не пуста:
    if not queue.empty():

        # Видалити заявку з черги з найвищим пріоритетом (мінімальним int)
        priority, request = queue.get()
        # Обробити заявку
        print(
            f"{Fore.BLUE}Опрацьовано: {request} пріоритет {prioritys[priority]:7}. Залишається в черзі: {queue.qsize()}{Style.RESET_ALL}"
        )

    # Інакше:
    else:
        # Вивести повідомлення, що черга пуста
        print(f"{Fore.GREEN}Всі заявки опрацьовані. Черга порожня.{Style.RESET_ALL}")


# ------------------------------------------------------------------------------

if __name__ == "__main__":

    # Створити чергу заявок
    # queue = Queue()
    queue = PriorityQueue()
    id_rqst = 0

    INFO = "Для завершення обробки натисніть Ctrl + C."
    print(INFO)
    # Головний цикл програми:
    try:
        # Поки користувач не вийде з програми:
        
        # Стовримо початкову чергу
        for _ in range(5):
            id_rqst = generate_request(queue, id_rqst)

        while True:
            if keyboard.is_pressed("esc"):
                print("Обробку перервано клавішею ESC.")
                break
            if random() <= 0.5:
                # Виконати generate_request() для створення нових заявок
                id_rqst = generate_request(queue, id_rqst)
            else:
                # Виконати process_request() для обробки заявок
                process_request(queue)
            pprint(queue.queue, width=20, sort_dicts=True)
            print(INFO)
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("Обробку перевано комбінацією <Ctrl+C> .")
