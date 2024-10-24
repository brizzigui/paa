# Implementação do Merge Sort para Análise de Tempo - parte 5 do trabalho 1 de PAA

import time
import random
import matplotlib.pyplot as plt

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

def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    return time.time() - start_time

def main():
    sizes = [100, 1000, 10000, 30000, 50000, 70000, 90000]
    execution_times = []

    for size in sizes:
        arr = random.sample(range(size * 10), size)
        
        exec_time = measure_time(merge_sort, arr)
        execution_times.append(exec_time)

    plt.plot(sizes, execution_times, label='Tempo de Execução', marker='o')
    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Tempo de Execução do Merge Sort')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
