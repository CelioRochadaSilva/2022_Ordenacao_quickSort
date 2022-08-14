ef partida(list, inicio, fim): #0(1)
    i = inicio
    pivot = list[fim]

    for j in range(inicio, fim): # O(1)  

        if list[j] <= pivot: #0(1)

            list[i], list[j] = list[j], list[i]
            i = i + 1 # ON  

    list[i], list[fim] = list[fim], list[i] #0(1)
    return i #0(1) 


def quickSort(list, inicio=0, fim=None):
    if fim is None:
        fim = len(list) - 1
    if inicio < fim:
        pivot = partida(list, inicio, fim)
        quickSort(list, inicio, pivot - 1)
        quickSort(list, pivot + 1, fim) # ON 


ar = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]  # LISTA DESORDENADA#
n = len(ar)
print(ar, " lista não ordenada")
quickSort(ar)
print(ar, " lista ordenada")
