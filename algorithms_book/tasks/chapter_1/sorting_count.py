# def count_sort(list_to_sort, largest_number=None):
#     if largest_number is None:
#         largest_number = max(list_to_sort)
#
#     check_list = [0] * (largest_number + 1)
#
#     for number in range(len(list_to_sort)):
#         check_list[list_to_sort[number]] += 1
#
#     check_list[0] -= 1
#
#     for number in range(1, largest_number + 1):
#         check_list[number] += check_list[number - 1]
#
#     result = [None] * len(list_to_sort)
#
#     for number in reversed(list_to_sort):
#         result[check_list[number]] = number
#         check_list[number] -= 1
#
#     return result


# def count_sort(list_to_sort, largest=None):
#     if largest is None:
#         largest = max(list_to_sort)
#
#     c = [0] * (largest + 1)
#
#     for i in range(len(list_to_sort)):
#         c[list_to_sort[i]] += 1
#
#     c[0] -= 1
#
#     print(f'{largest=}')
#     print(f'{len(c)=}')
#
#     for i in range(1, len(c)):
#         c[i] += c[i - 1]
#
#     result = [None] * len(list_to_sort)
#
#     for i in reversed(list_to_sort):
#         result[c[i]] = i
#         c[i] -= 1
#
#     return result


def count_sort(list_to_sort, largest=None):
    if largest is None:
        largest = max(list_to_sort)

    c = [0] * (largest + 1)

    for i in list_to_sort:
        c[i] += 1

    c[0] -= 1

    for i in range(1, largest+1):
        c[i] += c[i-1]

    result = [None] * len(list_to_sort)

    for i in list_to_sort:
        result[c[i]] = i
        c[i] -= 1

    return result


print(count_sort([5, 6, 11, 2, 0, 99, 99]))
