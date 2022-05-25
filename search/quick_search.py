def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]

    less = [i for i in lst[1:] if i < pivot]
    greater = [i for i in lst[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([1, 8, 9, 5, 44, 7]))
