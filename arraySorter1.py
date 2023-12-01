import numpy as np

def sorter1():
    # Upload the file array to the same folder
    arr = np.load('random_words_array.npy')
    arr_sorted = sorted(arr)