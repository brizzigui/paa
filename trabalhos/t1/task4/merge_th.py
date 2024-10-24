# Implementação do Merge Sort paralelo - parte 4 do trabalho 1 de PAA

import threading
import random

# Define um tamanho mínimo para a execução paralela do Merge Sort
THRESHOLD = 20000
# Define o tamanho do array
SIZE = 1000000
# Define o range de valores aleatórios
RANDOM_RANGE = 100000

# Função para mesclar dois subvetores ordenados em um único vetor ordenado
def merge(source, destination, left, mid, right):
    i = left
    j = mid + 1
    k = left

    # Une os arrays ordenados
    while i <= mid and j <= right:
        if source[i] < source[j]:
            destination[k] = source[i]
            i += 1
        else:
            destination[k] = source[j]
            j += 1
        k += 1

    # Copia os elementos restantes do subvetor esquerdo
    while i <= mid:
        destination[k] = source[i]
        i += 1
        k += 1

    # Copia os elementos restantes do subvetor direito
    while j <= right:
        destination[k] = source[j]
        j += 1
        k += 1


# Mergesort recursivo convencional
def mergesort(source, destination, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    mergesort(destination, source, left, mid)
    mergesort(destination, source, mid + 1, right)

    merge(source, destination, left, mid, right)


# Função recursiva paralela para o Merge Sort.
def pms_recursion(source, destination, left, right):
    if left >= right:
        return

    n = right - left + 1
    mid = (left + right) // 2

    if n > THRESHOLD:
        left_args = (destination, source, left, mid)
        right_args = (destination, source, mid + 1, right)

        left_thread = threading.Thread(target=pms_recursion, args=left_args)
        right_thread = threading.Thread(target=pms_recursion, args=right_args)

        left_thread.start()
        right_thread.start()

        left_thread.join()
        right_thread.join()
    else:
        mergesort(destination, source, left, mid)
        mergesort(destination, source, mid + 1, right)

    merge(source, destination, left, mid, right)


# Executa o Merge Sort de forma paralela.
def parallel_merge_sort(array):
    auxiliary = array.copy()
    pms_recursion(auxiliary, array, 0, len(array) - 1)


# Função para preencher um array de inteiros
def fill_array(array):
    for i in range(SIZE):
        array.append(random.randint(0, RANDOM_RANGE))


def main() -> None:
    array = []
    fill_array(array)

    parallel_merge_sort(array)

    print("Array ordenado com o merge sort paralelo")


if __name__ == "__main__":
    main()