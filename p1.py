import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
def measure_time(data):
    arr = data.copy()
    start = time.perf_counter()
    insertion_sort(arr)
    end = time.perf_counter()
    return end - start

sizes = [1000, 2000, 4000, 8000]

results = []

for n in sizes:
    print(f"Running for n = {n}")

    # Best Case 
    best_case = list(range(n))
    best_time = measure_time(best_case)

    # Average Case 
    avg_case = random.sample(range(n), n)
    avg_time = measure_time(avg_case)

    # Worst Case 
    worst_case = list(range(n, 0, -1))
    worst_time = measure_time(worst_case)

    results.append((n, best_time, avg_time, worst_time))



with open("insertion_sort_analysis.txt", "w") as f:

    f.write("Empirical Analysis of Insertion Sort\n")
    f.write("====================================\n\n")

    f.write("Theoretical Complexities:\n")
    f.write("Best Case    : Θ(n)\n")
    f.write("Average Case : Θ(n^2)\n")
    f.write("Worst Case   : Θ(n^2)\n\n")

    f.write("{:<10} {:<15} {:<15} {:<15}\n".format(
        "Input(n)", "Best Time(s)", "Average Time(s)", "Worst Time(s)"
    ))

    for r in results:
        f.write("{:<10} {:<15.6f} {:<15.6f} {:<15.6f}\n".format(*r))

    f.write("\nObservation:\n")
    f.write("Best case grows linearly.\n")
    f.write("Average and worst cases grow quadratically.\n")

print("Results saved to insertion_sort_analysis.txt")
