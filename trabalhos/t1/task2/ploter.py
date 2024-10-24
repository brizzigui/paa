import numpy as np
import matplotlib.pyplot as plt

def read_data(file_name):
    sizes = []
    heapsort_times = []
    quicksort_times = []
    mergesort_times = []
    timsort_times = []

    with open(file_name, 'r') as file:
        for line in file:
            values = eval(line.strip())
            sizes.append(values[0])
            heapsort_times.append(values[1])
            quicksort_times.append(values[2])
            mergesort_times.append(values[3])
            timsort_times.append(values[4])
    
    return sizes, heapsort_times, quicksort_times, mergesort_times, timsort_times

all_sizes = []
all_heapsort_times = []
all_quicksort_times = []
all_mergesort_times = []
all_timsort_times = []

for i in range(10):
    file_name = f'analise_{i}.txt'
    sizes, heapsort_times, quicksort_times, mergesort_times, timsort_times = read_data(file_name)

    all_sizes.append(sizes)
    all_heapsort_times.append(heapsort_times)
    all_quicksort_times.append(quicksort_times)
    all_mergesort_times.append(mergesort_times)
    all_timsort_times.append(timsort_times)

all_sizes = np.array(all_sizes)
all_heapsort_times = np.array(all_heapsort_times)
all_quicksort_times = np.array(all_quicksort_times)
all_mergesort_times = np.array(all_mergesort_times)
all_timsort_times = np.array(all_timsort_times)

mean_sizes = all_sizes[0] 
mean_heapsort_times = np.mean(all_heapsort_times, axis=0)
mean_quicksort_times = np.mean(all_quicksort_times, axis=0)
mean_mergesort_times = np.mean(all_mergesort_times, axis=0)
mean_timsort_times = np.mean(all_timsort_times, axis=0)

plt.figure(figsize=(10, 6))

plt.plot(mean_sizes, mean_heapsort_times, label='Heapsort', marker='o')
plt.plot(mean_sizes, mean_quicksort_times, label='Quicksort', marker='o')
plt.plot(mean_sizes, mean_mergesort_times, label='Mergesort', marker='o')
plt.plot(mean_sizes, mean_timsort_times, label='Timsort', marker='o')

plt.title('Tempo médio para ordenação x tamanho do vetor')
plt.xlabel('Tamanho do vetor')
plt.ylabel('Tempo (segundos)')
plt.legend()
plt.grid(True)
plt.show()
