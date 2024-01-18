list_to_sort = [5, 6, 88, 90, 1, 100, 7, 3, 2, 5]


def largest_two(a):
    """Find two largets numbers in a list

    Лучший случай: N - 1
    Худший: 2N - 3
    """
    my_max, second = a[:2]
    if my_max < second:
        my_max, second = second, my_max

    for number in a[2:]:
        if number > my_max:
            my_max, second = number, my_max
        elif number > second:
            second = number

    return my_max, second


print(largest_two(list_to_sort))


def sorting_two(a):
    return tuple(sorted(a, reverse=True)[:2])


print(sorting_two(list_to_sort))


def double_two(a):
    my_max = max(a)
    copy = list(a)
    copy.remove(my_max)
    return my_max, max(copy)


print(double_two(list_to_sort))


def mutable_two(a):
    idx = max(range(len(a)), key=a.__getitem__)  # трюк, позволяющий вернуть индекс максимального элемента
    my_max = a[idx]
    del a[idx]
    second = max(a)
    a.insert(idx, my_max)
    return my_max, second


print(mutable_two(list_to_sort))
