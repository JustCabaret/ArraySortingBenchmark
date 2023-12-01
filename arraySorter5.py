import numpy as np
import heapq

def sorter5():
    arr = np.load('random_words_array.npy').tolist()  # Converting numpy array to list

    # Use the heapq.heapify function
    heapq.heapify(arr)

    # Create a sorted array using heapq
    arr_sorted = [heapq.heappop(arr) for _ in range(len(arr))]
