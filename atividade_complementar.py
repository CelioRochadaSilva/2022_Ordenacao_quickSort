def partida(list, inicio, fim):
    i = inicio
    pivot = list[fim]

    for j in range(inicio, fim):

        if list[j] <= pivot:

            list[i], list[j] = list[j], list[i]
            i = i + 1

    list[i], list[fim] = list[fim], list[i]
    return i


def quickSort(list, inicio=0, fim=None):
    if fim is None:
        fim = len(list) - 1
    if inicio < fim:
        pivot = partida(list, inicio, fim)
        quickSort(list, inicio, pivot - 1)
        quickSort(list, pivot + 1, fim)


ar = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
n = len(ar)
print(ar, " lista não ordenada")
quickSort(ar)
print(ar, " lista ordenada")
