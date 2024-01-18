# def counting_sort(a, m):
#     # m = len(a)
#     counts = [0] * m
#     print(counts)
#     for v in range(len(a)):
#         print(v)
#         counts[v] += 1
#     pos = 0
#     v = 0
#     while pos < len(a):
#         for idx in range(counts[v]):
#             a[pos+idx] = v
#         pos += counts[v]
#         v += 1
#     print(a)
#
#
# counting_sort([3, 2, 1], 3)


# https://pythonist.ru/sortirovka-podschetom-na-python/
def counting_sort(alist, largest):
    # создается список размером с наибольшее число из списка на сортировку
    # в этот список записывается, сколько раз встречается каждое из чисел
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[alist[i]] += 1
    print(c)

    # Find the last index for each element
    c[0] = c[0] - 1  # to decrement each element for zero-based indexing
    # print(c)
    # print(c[0])
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]
    print(c)

    result = [None] * len(alist)

    # Though it is not required here,
    # it becomes necessary to reverse the list
    # when this function needs to be a stable sort

    # идем по списку, смотрим, какое значение в списке c у элемента с индексом == значение и списка alist
    for x in reversed(alist):
        result[c[x]] = x
        print(f'{x=}')
        print(f'{c[x]=}')
        c[x] = c[x] - 1  # если одинаковых значений несколько, сначала записываем в наибольший индекс и уменьшаем его
        print(result)

    return result


# alist = input('Enter the list of (nonnegative) numbers: ').split()
alist = [5, 76, 2, 4, 77, 77, 0, 0, 0]
alist = [int(x) for x in alist]
k = max(alist)
sorted_list = counting_sort(alist, k)
print('Sorted list: ', end='')
print(sorted_list)
