def get_chatbot_response(message):
    message = message.lower()
    if "bubble" in message:
        return "Bubble Sort is a simple algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order."
    elif "quick" in message:
        return "Quick Sort uses divide and conquer to efficiently sort elements by partitioning the list."
    elif "merge" in message:
        return "Merge Sort is a stable, divide-and-conquer algorithm with O(n log n) complexity."
    elif "best" in message:
        return "Each algorithm has its strengths. Quick Sort is usually fastest, Bubble Sort is simplest, and Merge Sort is good for stability."
    elif 'merge sort' in message:
        return "Merge Sort uses divide and conquer to sort arrays efficiently."
    elif 'best sorting' in message:
        return "For large datasets, Merge Sort or Quick Sort are usually preferred."
    elif "difference between bubble sort and selection sort" in message:
        return "Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order, while Selection Sort finds the minimum element and puts it at the beginning."

    elif "time complexity of insertion sort in the worst case" in message:
        return "The time complexity of Insertion Sort in the worst case is O(n²)."

    elif "fastest sorting algorithm for small datasets" in message:
        return "Insertion Sort is usually the fastest for small datasets because of its low overhead."

    elif "advantage of merge sort" in message:
        return "Merge Sort has a guaranteed time complexity of O(n log n) and is very efficient for large datasets."

    elif "quick sort faster in practice" in message:
        return "Quick Sort has good cache performance and low memory overhead compared to Merge Sort."

    elif "which sorting algorithm is stable" in message:
        return "Merge Sort and Insertion Sort are stable because they maintain the relative order of records with equal keys."

    elif "in-place sorting algorithm" in message:
        return "An in-place sorting algorithm uses constant extra space (O(1)) to rearrange the elements."

    elif "best-case time complexity of bubble sort" in message:
        return "The best-case time complexity of Bubble Sort is O(n), when the array is already sorted."

    elif "how does heap sort work" in message:
        return "Heap Sort builds a max heap from the input data, then repeatedly extracts the maximum element and rebuilds the heap."

    elif "applications of sorting algorithms" in message:
        return "Sorting algorithms are used in database query optimizations, data analysis, organizing records, and computer graphics."

    elif "avoid recursion sorting algorithm" in message:
        return "Heap Sort is a good choice because it can be implemented iteratively."

    elif "is counting sort comparison-based" in message:
        return "No, Counting Sort is not comparison-based; it sorts elements based on counting occurrences."

    elif "time complexity of counting sort" in message:
        return "The time complexity of Counting Sort is O(n + k), where n is the number of elements and k is the range of input."

    elif "problem with merge sort" in message:
        return "Merge Sort requires O(n) additional space, which can be problematic for very large datasets."

    elif "sorting algorithm for linked lists" in message:
        return "Merge Sort is preferred for linked lists because splitting and merging linked lists is efficient."


    else:
        return "I can help with sorting algorithms. Ask me about Bubble Sort, Quick Sort, or Merge Sort!"