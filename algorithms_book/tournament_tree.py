list_to_sort = [5, 6, 88, 90, 1, 100, 7, 3, 2, 5, 8, 9]
list_to_sort = [1, 1, 2, 1, 3, 1, 1, 10, 11]


def tournament_two(a):
    """медленный из-за памяти"""
    extra_number = None
    if len(list_to_sort) % 2 != 0:  # если длина нечетная, то обрезаем список, в конце сравним с этим элементом
        extra_number = list_to_sort.pop()
    n = len(a)
    winners = [None] * (n-1)
    losers = [None] * (n-1)
    prior = [-1] * (n-1)

    idx = 0
    for i in range(0, n, 2):
        if a[i] > a[i + 1]:
            winners[idx] = a[i]
            losers[idx] = a[i + 1]
        else:
            winners[idx] = a[i + 1]
            losers[idx] = a[i]
        idx += 1

    m = 0
    while idx < n - 1:
        print(f'{m=}')
        if winners[m] < winners[m + 1]:
            winners[idx] = winners[m+1]
            losers[idx] = winners[m]
            prior[idx] = m + 1
        else:
            winners[idx] = winners[m]
            losers[idx] = winners[m+1]
            prior[idx] = m
        m += 2
        idx += 1

    print(f'{winners=}')
    print(f'{losers=}')
    print(f'{prior=}')

    largest = winners[m]
    second = losers[m]
    m = prior[m]
    while m >= 0:
        if second < losers[m]:
            second = losers[m]
        m = prior[m]
        print(f'{m=}')

    if extra_number is not None:  # если длина списка нечетная
        if extra_number > largest:
            return extra_number, largest
        elif extra_number > second:
            return largest, extra_number

    return largest, second


print(tournament_two(list_to_sort))
