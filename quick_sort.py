import numpy as np

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def sorter4():
    # Upload the file array to the same folder
    arr = np.load('random_words_array.npy')
    # Use the function quick_sort
    arr_sorted_quick_sort = quick_sort(arr)