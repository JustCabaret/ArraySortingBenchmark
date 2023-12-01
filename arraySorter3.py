import numpy as np

def sorter3():
    # Upload the file array to the same folder
    arr = np.load('random_words_array.npy')

    # Use sorted function with a custom key
    arr_sorted = sorted(arr, key=lambda x: x.lower())
