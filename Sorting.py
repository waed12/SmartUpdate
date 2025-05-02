import time

def bubble_sort(arr):
    n = len(arr)
    comparisons = swaps = 0
    start = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    end = time.time()
    return arr, comparisons, swaps, end - start

def quick_sort(arr):
    comparisons = swaps = 0
    start = time.time()

    def partition(low, high):
        nonlocal comparisons, swaps
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def quick(low, high):
        if low < high:
            pi = partition(low, high)
            quick(low, pi - 1)
            quick(pi + 1, high)

    quick(0, len(arr) - 1)
    end = time.time()
    return arr, comparisons, swaps, end - start

def merge_sort(arr):
    comparisons = swaps = 0
    start = time.time()

    def merge(left, right):
        nonlocal comparisons, swaps
        result = []
        while left and right:
            comparisons += 1
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left + right
        swaps += len(result)
        return result

    def merge_sort_rec(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_rec(arr[:mid])
        right = merge_sort_rec(arr[mid:])
        return merge(left, right)

    sorted_arr = merge_sort_rec(arr)
    end = time.time()
    return sorted_arr, comparisons, swaps, end - start


def sort_array(array, algorithm):
    array = [int(x.strip()) for x in array if x.strip().isdigit()]
    if algorithm == 'Bubble Sort':
        sorted_arr, comp, swaps, duration = bubble_sort(array)
    elif algorithm == 'Quick Sort':
        sorted_arr, comp, swaps, duration = quick_sort(array)
    elif algorithm == 'Merge Sort':
        sorted_arr, comp, swaps, duration = merge_sort(array)
    else:
        return {"error": "Invalid algorithm selected."}

    return {
        "sorted_array": sorted_arr,
        "comparisons": comp,
        "swaps": swaps,
        "time": round(duration, 5)
    }
