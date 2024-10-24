# Implementação do Merge Sort - parte 1 do trabalho 1 de PAA

def merge(arr, left, mid, right):
    # Calcula o tamanho de cada array auxiliar
    size1 = mid - left + 1
    size2 = right - mid

    # Criar arrays auxliares
    aux_left = [0] * size1
    aux_right = [0] * size2

    # Copia para arrays auxiliares
    for i in range(size1):
        aux_left[i] = arr[left + i]
    for j in range(size2):
        aux_right[j] = arr[mid + 1 + j]

    i = 0 
    j = 0  
    k = left 

    # Une os arrays ordenadamente no array original
    while i < size1 and j < size2:
        if aux_left[i] <= aux_right[j]:
            arr[k] = aux_left[i]
            i += 1
        else:
            arr[k] = aux_right[j]
            j += 1
        k += 1

    # Readiciona os itens faltantes
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

        # Chamadas que dividem o array
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Chamada que faz merge
        merge(arr, left, mid, right)


# Função main
def main() -> None:
    # Lê entrada e converte em array de ints
    array = [*map(int, input("Digite inteiros separados por espaços: ").split())]
    merge_sort(array, 0, len(array)-1)

    print("O array ordenado é ", end="")
    print(array)


# Chama a main
if __name__ == "__main__":
    main()