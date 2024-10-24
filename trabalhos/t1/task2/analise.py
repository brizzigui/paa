import random
import time
import json

# Define o range de valores aleatórios
RANDOM_RANGE = 10000
MIN_MERGE = 32


# Quick sort
def partition(array, low, high):

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quickSort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)


# Merge sort
def merge(arr, left, mid, right):
    size1 = mid - left + 1
    size2 = right - mid

    aux_left = [0] * size1
    aux_right = [0] * size2

    for i in range(size1):
        aux_left[i] = arr[left + i]
    for j in range(size2):
        aux_right[j] = arr[mid + 1 + j]

    i = 0 
    j = 0  
    k = left 

    while i < size1 and j < size2:
        if aux_left[i] <= aux_right[j]:
            arr[k] = aux_left[i]
            i += 1
        else:
            arr[k] = aux_right[j]
            j += 1
        k += 1

    while i < size1:
        arr[k] = aux_left[i]
        i += 1
        k += 1

    while j < size2:
        arr[k] = aux_right[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


# Heap sort
def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i]) 
 
 
        heapify(arr, n, largest)
  
def heapSort(arr):
    n = len(arr)
 
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
 
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)


# Insertion sort
def insertionSort(arr, left, right): 
    for i in range(left + 1, right + 1): 
        j = i 
        while j > left and arr[j] < arr[j - 1]: 
            arr[j], arr[j - 1] = arr[j - 1], arr[j] 
            j -= 1

def calcMinRun(n): 
    r = 0
    while n >= MIN_MERGE: 
        r |= n & 1
        n >>= 1
    return n + r 

# Tim sort
def timSort(arr): 
    n = len(arr) 
    minRun = calcMinRun(n) 
  
    for start in range(0, n, minRun): 
        end = min(start + minRun - 1, n - 1) 
        insertionSort(arr, start, end) 
  
    size = minRun 
    while size < n: 
  
        for left in range(0, n, 2 * size): 
            
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
  
            if mid < right: 
                merge(arr, left, mid, right) 
  
        size = 2 * size 


# Função para preencher um array de inteiros
def fill_array_random(array, size):
    for i in range(size):
        array.append(random.randint(0, RANDOM_RANGE))


def main() -> None:
    array = []
    size = 0
    temp = []

    for i in range(0, 10):
        size = 0
        while(size < 1000000):
            if size < 100000:
                size = size + 10000
            else:
                size = size + 100000
            fill_array_random(array, size)
            temp.append(size)
            array2 = array.copy()
            array3 = array.copy()
            array4 = array.copy()


            t1 = time.perf_counter()
            heapSort(array)
            t2 = time.perf_counter()
            temp.append(t2 - t1)


            t3 = time.perf_counter()
            quickSort(array2, 0, len(array2) - 1)
            t4 = time.perf_counter()
            temp.append(t4 - t3)


            t5 = time.perf_counter()
            merge_sort(array3, 0, len(array3) - 1)
            t6 = time.perf_counter()
            temp.append(t6 - t5)


            t7 = time.perf_counter()
            timSort(array4)
            t8 = time.perf_counter()
            temp.append(t8 - t7)


            with open(f"analise_{i}.txt", "a") as f:
                json.dump(temp, f)
                f.write("\n")
            
            temp.clear()
            array.clear()
            array2.clear()
            array3.clear()
            array4.clear()

if __name__ == "__main__":
    main()