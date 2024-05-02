import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Generate random data for testing
data = [random.randint(0, 1000) for _ in range(1000)]

# Measure execution time for each sorting algorithm
merge_sort_time = timeit.timeit('merge_sort(data[:])', globals=globals(), number=100)
insertion_sort_time = timeit.timeit('insertion_sort(data[:])', globals=globals(), number=100)
timsort_time = timeit.timeit('sorted(data[:])', globals=globals(), number=100)

print("Merge Sort Time:", merge_sort_time)
print("Insertion Sort Time:", insertion_sort_time)
print("Timsort Time:", timsort_time)