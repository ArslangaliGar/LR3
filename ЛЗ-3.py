import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()

def bubble_sort(nums):
    logger.info("=" * 40)
    logger.info("НАЧАЛО СОРТИРОВКИ ПУЗЫРЬКОМ")
    logger.info(f"Исходный массив: {nums}")

    swapped = True
    pass_num = 0
    total_swaps = 0
    total_comparisons = 0

    while swapped:
        pass_num += 1
        swapped = False
        logger.info(f"\nПроход {pass_num}:")

        for i in range(len(nums) - 1):
            total_comparisons += 1
            logger.info(f"  Сравниваем элементы [{i}]={nums[i]} и [{i + 1}]={nums[i + 1]}")

            if nums[i] > nums[i + 1]:
                logger.info(f"    МЕНЯЕМ МЕСТАМИ: {nums[i]} <-> {nums[i + 1]}")
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
                total_swaps += 1
                logger.info(f" Массив сейчас: {nums}")
            else:
                logger.info(f" Не меняем ")

    logger.info(f"\n ИТОГ:")
    logger.info(f" Отсортированный массив: {nums}")
    logger.info(f" Всего проходов: {pass_num}")
    logger.info(f" Всего сравнений: {total_comparisons}")
    logger.info(f" Всего перестановок: {total_swaps}")
    logger.info("=" * 40 + "\n")
    return nums


def selection_sort(nums):
    logger.info("=" * 40)
    logger.info("НАЧАЛО СОРТИРОВКИ ВЫБОРОМ")
    logger.info(f"Исходный массив: {nums}")

    total_comparisons = 0
    total_swaps = 0

    for i in range(len(nums)):
        logger.info(f"\n Итерация {i + 1}: Ищем минимальный элемент начиная с позиции {i}")
        low_index = i
        logger.info(f"  Предполагаем, что минимальный элемент: nums[{i}] = {nums[i]}")

        for j in range(i + 1, len(nums)):
            total_comparisons += 1
            logger.info(f"    Сравниваем с nums[{j}] = {nums[j]}")

            if nums[j] < nums[low_index]:
                logger.info(f"      НАШЛИ МЕНЬШИЙ элемент! {nums[j]} < {nums[low_index]}")
                low_index = j

        if low_index != i:
            logger.info(f"  Меняем местами nums[{i}]={nums[i]} и nums[{low_index}]={nums[low_index]}")
            nums[i], nums[low_index] = nums[low_index], nums[i]
            total_swaps += 1
            logger.info(f"  Массив сейчас: {nums}")
        else:
            logger.info(f"  Минимальный элемент уже на месте (позиция {i})")

    logger.info(f"\nИТОГ:")
    logger.info(f"  Отсортированный массив: {nums}")
    logger.info(f"  Всего сравнений: {total_comparisons}")
    logger.info(f"  Всего перестановок: {total_swaps}")
    logger.info("=" * 40 + "\n")
    return nums


def insertion_sort(nums):
    logger.info("=" * 40)
    logger.info("НАЧАЛО СОРТИРОВКИ ВСТАВКАМИ")
    logger.info(f"Исходный массив: {nums}")

    total_comparisons = 0
    total_shifts = 0

    for i in range(1, len(nums)):
        logger.info(f"\n Итерация {i}: Обрабатываем элемент nums[{i}] = {nums[i]}")
        x = nums[i]
        j = i - 1
        logger.info(f" Будем искать место для {x} в отсортированной части [0..{i - 1}]")

        while j >= 0 and nums[j] > x:
            total_comparisons += 1
            logger.info(f" Сравниваем {x} с nums[{j}] = {nums[j]}")
            logger.info(f" Сдвигаем {nums[j]} вправо (из позиции {j} в позицию {j + 1})")
            nums[j + 1] = nums[j]
            total_shifts += 1
            j -= 1
            logger.info(f" Массив сейчас: {nums[:i + 1]} ...")

        if j >= 0:
            total_comparisons += 1
            logger.info(f" Сравниваем {x} с nums[{j}] = {nums[j]}")
            logger.info(f" {x} >= {nums[j]}, останавливаемся")

        logger.info(f" Вставляем {x} на позицию {j + 1}")
        nums[j + 1] = x
        logger.info(f" Массив после вставки: {nums[:i + 1]} ...")

    logger.info(f"\nИТОГ:")
    logger.info(f" Отсортированный массив: {nums}")
    logger.info(f" Всего сравнений: {total_comparisons}")
    logger.info(f" Всего сдвигов элементов: {total_shifts}")
    logger.info("=" * 40 + "\n")
    return nums


def heapify(nums, heap_size, root_index):
    logger.info(f" heapify: корень={root_index} (значение={nums[root_index]}), размер кучи={heap_size}")
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        logger.info(f" Левый потомок nums[{left_child}]={nums[left_child]} > текущего максимума {nums[largest]}")
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        logger.info(
            f" Правый потомок nums[{right_child}]={nums[right_child]} > текущего максимума {nums[largest]}")
        largest = right_child

    if largest != root_index:
        logger.info(f" МЕНЯЕМ: nums[{root_index}]={nums[root_index]} <-> nums[{largest}]={nums[largest]}")
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        logger.info(f" Массив после обмена: {nums}")
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    logger.info("=" * 40)
    logger.info("НАЧАЛО ПИРАМИДАЛЬНОЙ СОРТИРОВКИ")
    logger.info(f"Исходный массив: {nums}")

    n = len(nums)
    logger.info(f"Шаг 1: Построение max-кучи из {n} элементов")

    for i in range(n, -1, -1):
        logger.info(f" Вызываем heapify для корня {i}")
        heapify(nums, n, i)

    logger.info(f"Max-куча построена: {nums}")
    logger.info(f"\n Шаг 2: Извлечение элементов из кучи")

    for i in range(n - 1, 0, -1):
        logger.info(f" Итерация {n - i}: Меняем корень {nums[0]} с последним элементом {nums[i]}")
        nums[i], nums[0] = nums[0], nums[i]
        logger.info(f" Массив после обмена: {nums}")
        logger.info(f" Восстанавливаем свойства кучи для первых {i} элементов")
        heapify(nums, i, 0)

    logger.info(f"\n ИТОГ:")
    logger.info(f" Отсортированный массив: {nums}")
    logger.info("=" * 40 + "\n")
    return nums


def merge(left_list, right_list):
    logger.info(f" Сливаем {left_list} и {right_list}")
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                logger.info(f" Берем из левого списка: {left_list[left_list_index]}")
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                logger.info(f" Берем из правого списка: {right_list[right_list_index]}")
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            logger.info(f" Левый список закончился, берем из правого: {right_list[right_list_index]}")
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            logger.info(f" Правый список закончился, берем из левого: {left_list[left_list_index]}")
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    logger.info(f" Результат слияния: {sorted_list}")
    return sorted_list


def merge_sort(nums):
    logger.info(f" merge_sort: Вызываем для списка {nums}")

    if len(nums) <= 1:
        logger.info(f" Базовый случай: список из 1 элемента, возвращаем {nums}")
        return nums

    mid = len(nums) // 2
    logger.info(f" Разделяем список пополам. Середина: {mid}")
    logger.info(f" Левая половина: {nums[:mid]}")
    logger.info(f" Правая половина: {nums[mid:]}")

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    result = merge(left_list, right_list)
    logger.info(f" merge_sort: Возвращаем результат: {result}")
    return result


def partition(nums, low, high):
    logger.info(f" partition: low={low}, high={high}")
    logger.info(f" Подмассив для разделения: {nums[low:high + 1]}")

    pivot = nums[(low + high) // 2]
    logger.info(f" Опорный элемент: nums[{(low + high) // 2}] = {pivot}")

    i = low - 1
    j = high + 1
    logger.info(f" Начальные индексы: i={i}, j={j}")

    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
            logger.info(f" i увеличено до {i}, nums[{i}]={nums[i]}")

        j -= 1
        while nums[j] > pivot:
            j -= 1
            logger.info(f" j уменьшено до {j}, nums[{j}]={nums[j]}")

        logger.info(f" После внутренних циклов: i={i}, nums[i]={nums[i]}, j={j}, nums[j]={nums[j]}")

        if i >= j:
            logger.info(f" i >= j ({i} >= {j}), возвращаем j={j} как точку разделения")
            return j

        logger.info(f" Меняем местами nums[{i}]={nums[i]} и nums[{j}]={nums[j]}")
        nums[i], nums[j] = nums[j], nums[i]
        logger.info(f" Подмассив после обмена: {nums[low:high + 1]}")


def quick_sort(nums):
    logger.info("=" * 40)
    logger.info("НАЧАЛО БЫСТРОЙ СОРТИРОВКИ")
    logger.info(f"Исходный массив: {nums}")

    def _quick_sort(items, low, high):
        logger.info(f" Быстрая сортировка: low={low}, high={high}, подмассив={items[low:high + 1]}")

        if low < high:
            split_index = partition(items, low, high)
            logger.info(f" Точка разделения: {split_index}")
            logger.info(f" Рекурсивно сортируем левую часть: {items[low:split_index + 1]}")
            _quick_sort(items, low, split_index)
            logger.info(f" Рекурсивно сортируем правую часть: {items[split_index + 1:high + 1]}")
            _quick_sort(items, split_index + 1, high)
        else:
            logger.info(f" Базовый случай: low >= high, выходим")

    _quick_sort(nums, 0, len(nums) - 1)
    logger.info(f"\nИТОГ:")
    logger.info(f" Отсортированный массив: {nums}")
    logger.info("=" * 40 + "\n")
    return nums


if __name__ == "__main__":
    logger.disabled = True

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМОВ СОРТИРОВКИ")
    print("=" * 60)

    test_arrays = {
        "Пузырьковая сортировка": [5, 2, 1, 8, 4,10,12,2,3,27,18,6],
        "Сортировка выбором": [12, 8, 3, 20, 11,10,12,2,3,27,18,6],
        "Сортировка вставками": [9, 1, 15, 28, 6,10,12,2,3,27,18,6],
        "Пирамидальная сортировка": [35, 12, 43, 8, 51,10,12,2,3,27,18,6],
        "Быстрая сортировка": [22, 5, 1, 18, 99,10,12,2,3,27,18,6]
    }

    for algo_name, array in test_arrays.items():
        print(f"\n{'=' * 60}")
        print(f"{algo_name.upper()}")
        print(f"{'=' * 60}")

        logger.disabled = False

        test_array = array.copy()

        if algo_name == "Пузырьковая сортировка":
            result = bubble_sort(test_array)
        elif algo_name == "Сортировка выбором":
            result = selection_sort(test_array)
        elif algo_name == "Сортировка вставками":
            result = insertion_sort(test_array)
        elif algo_name == "Пирамидальная сортировка":
            result = heap_sort(test_array)
        elif algo_name == "Быстрая сортировка":
            result = quick_sort(test_array)

        print(f"Результат: {result}")

        logger.disabled = True

    print(f"\n{'=' * 60}")
    print(f"СОРТИРОВКА СЛИЯНИЕМ")
    print(f"{'=' * 60}")

    logger.disabled = False
    test_array = [120, 45, 68, 250, 176]
    print(f"Исходный массив: {test_array}")
    result = merge_sort(test_array.copy())
    print(f"Результат: {result}")
    logger.disabled = True

    print(f"\n{'=' * 60}")
    print(f"{'=' * 60}")