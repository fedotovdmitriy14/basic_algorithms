def quicksort(array: list):
    if len(array) == 0:
        return array

    pivot = array[0]

    lower = [el for el in array if el < pivot]
    higher = [el for el in array if el > pivot]
    mid = [el for el in array if el == pivot]
    # print(f'{pivot=}, {lower=}, {higher=}, {mid=}')

    return (
        quicksort(lower) +
        mid +
        quicksort(higher)
    )


print(quicksort([9, 7, 1, 5, 66, 0, 88]))
