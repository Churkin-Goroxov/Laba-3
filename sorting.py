import logging

# Создание логгера
sorting_logger = logging.getLogger(__name__)
sorting_logger.setLevel(logging.INFO)

# Настройка
file_handler = logging.FileHandler("sorting.log", mode='w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
file_handler.setFormatter(formatter)
sorting_logger.addHandler(file_handler)


class IterationCounter:
    """Класс для подсчета итераций"""

    def __init__(self):
        self.count = 0

    def reset(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count


# Глобальный счетчик итераций
iteration_counter = IterationCounter()


def buble_sort(a):
    iteration_counter.reset()
    try:
        sorting_logger.info(f"Начало buble_sort с массивом из {len(a)} элементов")
        n = len(a)
        for i in range(n - 1):
            for j in range(n - 1, i, -1):
                iteration_counter.increment()
                if a[j] < a[j - 1]:
                    a[j], a[j - 1] = a[j - 1], a[j]
        sorting_logger.info(f"Завершение buble_sort. Итераций: {iteration_counter.get_count()}")
        return iteration_counter.get_count()
    except Exception as e:
        sorting_logger.error(f"Ошибка в buble_sort", exc_info=True)
        raise


def buble_sort_fl(a):
    iteration_counter.reset()
    try:
        sorting_logger.info(f"Начало buble_sort_fl с массивом из {len(a)} элементов")
        n = len(a)
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                iteration_counter.increment()
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True
            if not swapped:
                break
        sorting_logger.info(f"Завершение buble_sort_fl. Итераций: {iteration_counter.get_count()}")
        return iteration_counter.get_count()
    except Exception as e:
        sorting_logger.error(f"Ошибка в buble_sort_fl", exc_info=True)
        raise


def choise_sort(a):
    iteration_counter.reset()
    try:
        sorting_logger.info(f"Начало choise_sort с массивом из {len(a)} элементов")
        n = len(a)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                iteration_counter.increment()
                if a[j] < a[min_idx]:
                    min_idx = j
            if min_idx != i:
                a[i], a[min_idx] = a[min_idx], a[i]
        sorting_logger.info(f"Завершение choise_sort. Итераций: {iteration_counter.get_count()}")
        return iteration_counter.get_count()
    except Exception as e:
        sorting_logger.error(f"Ошибка в choise_sort", exc_info=True)
        raise


def gnome_sort(a):
    iteration_counter.reset()
    try:
        sorting_logger.info(f"Начало gnome_sort с массивом из {len(a)} элементов")
        n = len(a)
        i = 1
        while i < n:
            iteration_counter.increment()
            if a[i] >= a[i - 1]:
                i += 1
            else:
                a[i], a[i - 1] = a[i - 1], a[i]
                if i > 1:
                    i -= 1
        sorting_logger.info(f"Завершение gnome_sort. Итераций: {iteration_counter.get_count()}")
        return iteration_counter.get_count()
    except Exception as e:
        sorting_logger.error(f"Ошибка в gnome_sort", exc_info=True)
        raise


def insert_sort(a):
    iteration_counter.reset()
    try:
        sorting_logger.info(f"Начало insert_sort с массивом из {len(a)} элементов")
        n = len(a)
        for i in range(1, n):
            key = a[i]
            j = i - 1
            while j >= 0 and a[j] > key:
                iteration_counter.increment()
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key
            iteration_counter.increment()  # Считаем внешний цикл
        sorting_logger.info(f"Завершение insert_sort. Итераций: {iteration_counter.get_count()}")
        return iteration_counter.get_count()
    except Exception as e:
        sorting_logger.error(f"Ошибка в insert_sort", exc_info=True)
        raise


def heapify(a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] > a[largest]:
        largest = left

    if right < n and a[right] > a[largest]:
        largest = right

    if largest != i:
        iteration_counter.increment()
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)


def heap_sort(a):
    iteration_counter.reset()
    try:
        sorting_logger.info(f"Начало heap_sort с массивом из {len(a)} элементов")
        n = len(a)

        # Построение max-heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(a, n, i)
            iteration_counter.increment()

        # Извлечение элементов из кучи
        for i in range(n - 1, 0, -1):
            iteration_counter.increment()
            a[i], a[0] = a[0], a[i]
            heapify(a, i, 0)

        sorting_logger.info(f"Завершение heap_sort. Итераций: {iteration_counter.get_count()}")
        return iteration_counter.get_count()
    except Exception as e:
        sorting_logger.error(f"Ошибка в heap_sort", exc_info=True)
        raise


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        iteration_counter.increment()
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(a):
    iteration_counter.reset()
    try:
        sorting_logger.info(f"Начало merge_sort с массивом из {len(a)} элементов")

        def _merge_sort(arr):
            if len(arr) <= 1:
                return arr

            iteration_counter.increment()
            mid = len(arr) // 2
            left = _merge_sort(arr[:mid])
            right = _merge_sort(arr[mid:])
            return merge(left, right)

        result = _merge_sort(a)
        sorting_logger.info(f"Завершение merge_sort. Итераций: {iteration_counter.get_count()}")
        return result
    except Exception as e:
        sorting_logger.error(f"Ошибка в merge_sort", exc_info=True)
        raise


def partition(a, low, high):
    pivot = a[high]
    i = low - 1

    for j in range(low, high):
        iteration_counter.increment()
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def quick_sort(a):
    iteration_counter.reset()
    try:
        sorting_logger.info(f"Начало quick_sort с массивом из {len(a)} элементов")

        def _quick_sort(arr, low, high):
            if low < high:
                iteration_counter.increment()
                pi = partition(arr, low, high)
                _quick_sort(arr, low, pi - 1)
                _quick_sort(arr, pi + 1, high)

        _quick_sort(a, 0, len(a) - 1)
        sorting_logger.info(f"Завершение quick_sort. Итераций: {iteration_counter.get_count()}")
        return iteration_counter.get_count()
    except Exception as e:
        sorting_logger.error(f"Ошибка в quick_sort", exc_info=True)
        raise