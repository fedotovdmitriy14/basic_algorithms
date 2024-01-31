def insertion_sort(a):
    """Сортировка вставками.
    Наихудший случай - значения, упорядоченные по убыванию. Дает N x (N-1) сравнений и столько же обменов.
    """
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j-1] <= a[j]:
                break
            a[j], a[j-1] = a[j-1], a[j]
    return a


print(insertion_sort([1, 9, 90, 5, 6, -8]))
