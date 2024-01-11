# Array-Sorting-Benchmark
This project benchmarks and compares the performance and energy efficiency of five different array sorting algorithms. The algorithms are implemented in separate files: `built_in_sort.py`, `merge_sort.py`, `case_insensitive_sort.py`, `quick_sort.py`, and `heap_sort.py`. Additionally, there is an array generator script, `array_generator.py`, to create sample arrays for testing.

## Algorithms

1. **Built-in Sort:** This algorithm uses the built-in sorted function in Python to sort an array of words loaded from a file (`random_words_array.npy`).
2. **Merge Sort:** Implementation of the merge sort algorithm. It recursively divides the array into halves, sorts them, and then merges them back together.
3. **Case-Insensitive Sort:** Utilizes the sorted function with a custom key to perform a case-insensitive sorting of the array loaded from the file (`random_words_array.npy`).
4. **Quick Sort:** Implements the quicksort algorithm to sort an array of words loaded from a file (`random_words_array.npy`).
5. **Heap Sort:** This algorithm uses the heapq module to perform an in-place heap sort on the array of words loaded from a file (`random_words_array.npy`). The array is converted to a list before applying heap sort.

## Array Generator

The `array_generator.py` script generates an array of random words and saves it to a binary file (`random_words_array.npy`) for testing the sorting algorithms.

## Running the Benchmark
To run the benchmark and generate performance metrics and energy efficiency scores, execute the `energy_counter.py` script.

```python energy_counter.py```

## Results and Visualizations
The benchmark results are visualized using matplotlib, displaying metrics such as memory consumption, average CPU usage, peak CPU usage, execution time, and energy efficiency scores.

## Interpretation of Energy Efficiency Scores
The energy efficiency score is calculated as the ratio of execution time to peak CPU usage. Lower scores indicate better energy efficiency.

## Conclusion
After running the benchmark, the script identifies and prints the most energy-efficient sorting algorithm based on the calculated scores.

## Dependencies
1. Python 3
2. NumPy
3. Matplotlib
4. Psutil

Install dependencies using:

```pip install numpy matplotlib psutil``` 

This project was made with the help of @Bita05.
Feel free to contribute, report issues, or suggest improvements!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
