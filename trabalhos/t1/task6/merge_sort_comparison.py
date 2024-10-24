# Implementação do Merge Sort Recursivo e Iterativo - parte 6 do trabalho 1 de PAA

import time
import random
import matplotlib.pyplot as plt

# Implementação recursiva
def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid])
    right = merge_sort_recursive(arr[mid:])
    return merge(left, right)

# Faz o Merge (tanto para a implementação recursiva quanto para a iterativa)
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

# Implementação iterativa
def merge_sort_iterative(arr):
    width = 1
    n = len(arr)
    result = arr.copy()
    while width < n:
        for i in range(0, n, 2 * width):
            left = result[i:i + width]
            right = result[i + width:i + 2 * width]
            result[i:i + 2 * width] = merge(left, right)
        width *= 2
    return result

def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    return time.time() - start_time

def main():
    sizes = [100, 500, 1000, 5000, 10000, 100000]
    recursive_times = []
    iterative_times = []

    for size in sizes:
        arr = random.sample(range(size * 10), size)
        
        rec_time = measure_time(merge_sort_recursive, arr)
        it_time = measure_time(merge_sort_iterative, arr)

        recursive_times.append(rec_time)
        iterative_times.append(it_time)

    plt.plot(sizes, recursive_times, label='Recursivo', marker='o')
    plt.plot(sizes, iterative_times, label='Iterativo', marker='s')
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Tempo de execução (segundos)')
    plt.title('Comparação de Desempenho: Merge Sort Recursivo vs Iterativo')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
