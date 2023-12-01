import os
import psutil
from threading import Thread
import time
import matplotlib.pyplot as plt
from arraySorter1 import sorter1
from arraySorter2 import sorter2
from arraySorter3 import sorter3
from arraySorter4 import sorter4
from arraySorter5 import sorter5

# Function to monitor CPU usage, allocate memory, and measure execution time
def monitor_cpu_memory_time(func, results, interval_seconds=1):
    cpu_usage_values = []

    # Function to monitor CPU usage
    def monitor_cpu():
        while thread.is_alive():
            cpu_percent = psutil.cpu_percent(interval=interval_seconds)
            print(f"CPU Usage: {cpu_percent}%")
            cpu_usage_values.append(cpu_percent)

    # Start the function in a separate thread
    thread = Thread(target=func)
    thread.start()

    # Measure execution time
    start_time = time.time()

    # Monitor CPU usage
    monitor_cpu()

    # Wait for the function to complete
    thread.join()

    # Calculate average and peak CPU usage correctly
    avg_cpu_usage = sum(cpu_usage_values) / len(cpu_usage_values) if cpu_usage_values else 0
    peak_cpu_usage = max(cpu_usage_values) if cpu_usage_values else 0

    # Measure execution time
    end_time = time.time()
    execution_time = end_time - start_time

    # Measure and print memory usage
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    memory_consumption = mem_info.rss / (1024 ** 2)

    # Calculate energy efficiency score
    energy_efficiency_score = execution_time / peak_cpu_usage if peak_cpu_usage != 0 else 0

    print(f"\nMetrics for {func.__name__}:")
    print(f"Memory Consumption: {memory_consumption:.2f} MB")
    print(f"Average CPU Usage: {avg_cpu_usage:.2f}%")
    print(f"Peak CPU Usage: {peak_cpu_usage}%")
    print(f"Execution Time: {execution_time:.2f} seconds")
    print(f"Energy Efficiency Score: {energy_efficiency_score:.2f}")

    # Register results
    results[func.__name__] = (memory_consumption, avg_cpu_usage, peak_cpu_usage, execution_time, energy_efficiency_score)

# Function to create bar charts and evaluate energy efficiency
def create_bar_charts(results):
    names, data = zip(*results.items())
    memory_consumption, avg_cpu_usage, peak_cpu_usage, execution_time, energy_efficiency_score = zip(*data)

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle('Metrics by Algorithm')

    # Memory Consumption Bar Chart
    axes[0, 0].bar(names, memory_consumption)
    axes[0, 0].set_title('Memory Consumption (MB)')
    axes[0, 0].set_ylabel('MB')

    # Average CPU Usage Bar Chart
    axes[0, 1].bar(names, avg_cpu_usage)
    axes[0, 1].set_title('Average CPU Usage (%)')
    axes[0, 1].set_ylabel('%')

    # Peak CPU Usage Bar Chart
    axes[1, 0].bar(names, peak_cpu_usage)
    axes[1, 0].set_title('Peak CPU Usage (%)')
    axes[1, 0].set_ylabel('%')

    # Execution Time Bar Chart
    axes[1, 1].bar(names, execution_time)
    axes[1, 1].set_title('Execution Time (s)')
    axes[1, 1].set_ylabel('s')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    # Initialize the list of functions to test
    functions_to_test = [
        ("sorter1", sorter1),
        ("sorter2", sorter2),
        ("sorter3", sorter3),
        ("sorter4", sorter4),
        ("sorter5", sorter5)
    ]

    # Initialize the results registry
    all_results = {}

    # Test and monitor each function individually
    for name, function in functions_to_test:
        print(f"\n=== Testing {name} ===")
        monitor_cpu_memory_time(function, all_results)

    # Create charts
    create_bar_charts(all_results)

    # Identify the most energy-efficient algorithm
    most_efficient_energy_algorithm = min(all_results.items(), key=lambda x: x[1][-1])

    print(f"\nThe most energy-efficient algorithm is {most_efficient_energy_algorithm[0]} with a score of {most_efficient_energy_algorithm[1][-1]:.2f}")
