# def bsearch(elements, k):
#     lo = 0
#     hi = len(elements)
#
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         print(mid)
#
#         if k == elements[mid]:
#             return k
#         elif elements[mid] > k:
#             hi = mid - 1
#         elif elements[mid] < k:
#             lo = mid + 1
#
#     return -lo


def bsearch(el, k):
    lo = 0
    hi = len(el)

    while lo <= hi:
        mid = (lo + hi) // 2

        print(f'{mid=}')

        if el[mid] == k:
            print(f'{mid=}')
            return mid
        if el[mid] > k:
            hi = mid - 1
        elif el[mid] < k:
            lo = mid + 1

    return lo + 1


print(bsearch(list(range(890)), 90))
# print(bsearch([1, 2, 3, 90, 91], 90))
