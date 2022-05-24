test_array = [i+2 for i in range(99)]


def bin_search(lst, number):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = int((low + high) / 2)
        print(f'{mid=}')
        guess = lst[mid]
        if guess == number:
            return mid
        if guess > number:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(bin_search(test_array, 52))
