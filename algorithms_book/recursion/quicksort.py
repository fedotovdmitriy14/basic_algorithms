def quicksort(array: list, reverse: bool = False):
    if len(array) == 0:
        return array

    pivot = array[0]

    lower = [el for el in array if el < pivot]
    higher = [el for el in array if el > pivot]
    mid = [el for el in array if el == pivot]
    # print(f'{pivot=}, {lower=}, {higher=}, {mid=}')

    if reverse:
        return (
                quicksort(higher, reverse) +
                mid +
                quicksort(lower, reverse)
        )
    return (
        quicksort(lower, reverse) +
        mid +
        quicksort(higher, reverse)
    )


print(quicksort([9, 7, 1, 5, 66, 0, 88], reverse=True))
