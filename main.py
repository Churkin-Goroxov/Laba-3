from sorting import *
import logging
import random
import time

# Создание логгера
main_logger = logging.getLogger(__name__)
main_logger.setLevel(logging.INFO)

# Настройка
main_handler = logging.FileHandler("main.log", mode='w')
main_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
main_handler.setFormatter(main_formatter)
main_logger.addHandler(main_handler)


def generate_random_list(size=100):
    return [random.randint(1, 1000) for _ in range(size)]


def run_all_sorts(original_list):
    sorting_functions = [
        ("Пузырьковая сортировка", buble_sort),
        ("Пузырьковая сортировка с флагом", buble_sort_fl),
        ("Сортировка выбором", choise_sort),
        ("Гномья сортировка", gnome_sort),
        ("Сортировка вставками", insert_sort),
        ("Пирамидальная сортировка", heap_sort),
        ("Сортировка слиянием", merge_sort),
        ("Быстрая сортировка", quick_sort)
    ]

    for name, sort_func in sorting_functions:
        try:
            main_logger.info(f"Запуск {name}")
            arr_copy = original_list.copy()

            start_time = time.time()

            if sort_func == merge_sort:
                result = sort_func(arr_copy)
                execution_time = time.time() - start_time
                print(f"{name:35} | Время: {execution_time:.6f} сек")
            else:
                sort_func(arr_copy)
                execution_time = time.time() - start_time
                print(f"{name:35} | Время: {execution_time:.6f} сек")

            main_logger.info(f"Завершение {name}. Время выполнения: {execution_time:.6f} секунд")
            print()

        except Exception as e:
            main_logger.error(f"Ошибка в {name}", exc_info=True)
            print(f"{name}: Ошибка - {e}")
            print()


def run_single_sort(original_list, choice):
    sorting_map = {
        1: ("Пузырьковая сортировка", buble_sort),
        2: ("Пузырьковая сортировка с флагом", buble_sort_fl),
        3: ("Сортировка выбором", choise_sort),
        4: ("Гномья сортировка", gnome_sort),
        5: ("Сортировка вставками", insert_sort),
        6: ("Пирамидальная сортировка", heap_sort),
        7: ("Сортировка слиянием", merge_sort),
        8: ("Быстрая сортировка", quick_sort)
    }

    if choice in sorting_map:
        name, sort_func = sorting_map[choice]
        try:
            main_logger.info(f"Запуск {name}")
            arr_copy = original_list.copy()

            # Замер времени выполнения
            start_time = time.time()

            if sort_func == merge_sort:
                result = sort_func(arr_copy)
                execution_time = time.time() - start_time
                print(f"\n{name}")
                print(f"Время выполнения: {execution_time:.6f} секунд")
                print(f"Результат: {result}")
                main_logger.info(f"Результат {name}: {result}")
            else:
                sort_func(arr_copy)
                execution_time = time.time() - start_time
                print(f"\n{name}")
                print(f"Время выполнения: {execution_time:.6f} секунд")
                print(f"Результат: {arr_copy}")
                main_logger.info(f"Результат {name}: {arr_copy}")

            main_logger.info(f"Завершение {name}. Время выполнения: {execution_time:.6f} секунд")

        except Exception as e:
            main_logger.error(f"Ошибка в {name}", exc_info=True)
            print(f"Ошибка в {name}: {e}")
    else:
        print("Неверный выбор!")


main_logger.info("Программа запущена")

random_list_of_nums = generate_random_list(10000)
main_logger.info(f"Исходный массив: {random_list_of_nums}")
print(f"Исходный массив ({len(random_list_of_nums)} элементов):")
print(random_list_of_nums)
print()

while True:
    print("\nВыберите действие:")
    print("1 - Пузырьковая сортировка")
    print("2 - Пузырьковая сортировка с флагом")
    print("3 - Сортировка выбором")
    print("4 - Гномья сортировка")
    print("5 - Сортировка вставками")
    print("6 - Пирамидальная сортировка")
    print("7 - Сортировка слиянием")
    print("8 - Быстрая сортировка")
    print("9 - Запустить все сортировки")
    print("0 - Выход")

    try:
        choice = int(input("Введите цифру: "))

        if choice == 0:
            main_logger.info("Завершение программы")
            print("Выход из программы")
            break
        elif choice == 9:
            main_logger.info("Запуск всех сортировок")
            run_all_sorts(random_list_of_nums)
            main_logger.info("Все сортировки завершены")
        elif 1 <= choice <= 8:
            run_single_sort(random_list_of_nums, choice)
        else:
            print("Неверный выбор! Попробуйте снова.")

    except ValueError:
        print("Ошибка: введите целое число!")
    except Exception as e:
        main_logger.error("Неожиданная ошибка", exc_info=True)
        print(f"Произошла ошибка: {e}")