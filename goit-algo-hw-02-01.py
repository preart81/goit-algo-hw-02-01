"""Програма, яка імітує приймання й обробку заявок: 
програма має автоматично генерувати нові заявки 
(ідентифіковані унікальним номером або іншими даними), 
додавати їх до черги, а потім послідовно видаляти з черги для
"обробки", імітуючи таким чином роботу сервісного центру."""

from colorama import Fore, Style, init as colorama_init
from pprint import pprint
from queue import Queue, PriorityQueue
from random import random, choice
import keyboard
import time

# Пріоритети заявок

prioritys = {
    0: "High",
    1: "Normal",
}


# Функція generate_request():
def generate_request(queue, id_rqst):
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
def process_request():
    global queue, id_rqst
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

    info = print("Для завершення обробки натисніть Ctrl + C.")
    # Головний цикл програми:
    try:
        # Поки користувач не вийде з програми:
        while True:
            if keyboard.is_pressed("esc"):
                print("Обробку перервано клавішею ESC.")
                break
            if random() <= 0.5:
                # Виконати generate_request() для створення нових заявок
                id_rqst = generate_request(queue, id_rqst)
            else:
                # Виконати process_request() для обробки заявок
                process_request()
            pprint(queue.queue, width=20, sort_dicts=False)
            time.sleep(1.0)
    except KeyboardInterrupt:
        print(f"Обробку перевано комбінацією <Ctrl+C> .")
