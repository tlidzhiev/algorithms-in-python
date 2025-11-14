import random
import time

import matplotlib.pyplot as plt
import numpy as np
from makeheap import makeheap, makeheap_n_log_n


def measure_time(func, arr, num_runs=5):
    times = []

    for _ in range(num_runs):
        arr_copy = arr.copy()
        start = time.perf_counter()
        func(arr_copy)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)


def run_benchmark(sizes, num_runs=10):
    times_n_log_n = []
    times_n = []

    for size in sizes:
        arr = [random.randint(1, 100000) for _ in range(size)]

        time_n_log_n = measure_time(makeheap_n_log_n, arr, num_runs)
        times_n_log_n.append(time_n_log_n)

        time_n = measure_time(makeheap, arr, num_runs)
        times_n.append(time_n)

    return sizes, times_n_log_n, times_n


def plot_results(sizes, times_n_log_n, times_n):
    sizes = np.array(sizes)
    times_n_log_n = np.array(times_n_log_n)
    times_n = np.array(times_n)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Heap Construction Algorithms: Empirical Complexity Analysis',
                 fontsize=16, fontweight='bold')

    # Plot 1: Direct comparison of execution times
    ax1 = axes[0, 0]
    ax1.plot(sizes, times_n_log_n * 1000, 'o-', label='makeheap_n_log_n',
             linewidth=2, markersize=6, color='red')
    ax1.plot(sizes, times_n * 1000, 's-', label='makeheap',
             linewidth=2, markersize=6, color='blue')
    ax1.set_xlabel('Array Size (N)', fontsize=11)
    ax1.set_ylabel('Time (ms)', fontsize=11)
    ax1.set_title('Execution Time Comparison', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)

    # Plot 2: Normalized by N (should show O(log N) vs O(1))
    ax2 = axes[0, 1]
    ax2.plot(sizes, (times_n_log_n * 1000) / sizes, 'o-',
             label='makeheap_n_log_n / N', linewidth=2, markersize=6, color='red')
    ax2.plot(sizes, (times_n * 1000) / sizes, 's-',
             label='makeheap / N', linewidth=2, markersize=6, color='blue')
    ax2.set_xlabel('Array Size (N)', fontsize=11)
    ax2.set_ylabel('Time / N (ms)', fontsize=11)
    ax2.set_title('Time Normalized by N', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)

    # Plot 3: Time vs N*log(N) for makeheap_n_log_n (should be linear)
    ax3 = axes[1, 0]
    n_log_n = sizes * np.log2(sizes)
    coeffs_nlogn = np.polyfit(n_log_n, times_n_log_n * 1000, 1)
    fit_nlogn = np.poly1d(coeffs_nlogn)

    ax3.scatter(n_log_n, times_n_log_n * 1000, color='red', s=50, alpha=0.6,
                label='Measured data')
    ax3.plot(n_log_n, fit_nlogn(n_log_n), 'r--', linewidth=2,
             label=f'Linear fit: y = {coeffs_nlogn[0]:.6f}x + {coeffs_nlogn[1]:.4f}')
    ax3.set_xlabel('N * log(N)', fontsize=11)
    ax3.set_ylabel('Time (ms)', fontsize=11)
    ax3.set_title('makeheap_n_log_n: Verifying O(N log N)',
                  fontsize=12, fontweight='bold')
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3)

    # Plot 4: Time vs N for makeheap (should be linear)
    ax4 = axes[1, 1]
    coeffs_n = np.polyfit(sizes, times_n * 1000, 1)
    fit_n = np.poly1d(coeffs_n)

    ax4.scatter(sizes, times_n * 1000, color='blue', s=50, alpha=0.6,
                label='Measured data')
    ax4.plot(sizes, fit_n(sizes), 'b--', linewidth=2,
             label=f'Linear fit: y = {coeffs_n[0]:.6f}x + {coeffs_n[1]:.4f}')
    ax4.set_xlabel('N', fontsize=11)
    ax4.set_ylabel('Time (ms)', fontsize=11)
    ax4.set_title('makeheap: Verifying O(N)', fontsize=12, fontweight='bold')
    ax4.legend(fontsize=9)
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()

    filename = 'heap_complexity_analysis.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"\nGraph saved as '{filename}'")

    plt.show()


def main():
    sizes = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
    num_runs = 100
    sizes, times_n_log_n, times_n = run_benchmark(sizes, num_runs)
    plot_results(sizes, times_n_log_n, times_n)


if __name__ == "__main__":
    main()
