def selection_sort(to_sort):
    """Сортировка выбором.
    N x (N-1) сравнений и N-1 обменов.
    """
    n = len(to_sort)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if to_sort[j] < to_sort[min_index]:
                min_index = j

            to_sort[i], to_sort[min_index] = to_sort[min_index], to_sort[i]

    return to_sort


print(selection_sort([9, 90, 4, 5, 1, 88]))
