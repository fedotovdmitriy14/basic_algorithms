import timeit


def is_palindrome(p):
    idx_start = 0
    idx_finish = len(p) - 1
    while idx_start < idx_finish:
        if p[idx_start] in (' ', ',', '!') or p[idx_finish] in (' ', ',', '!'):
            idx_start += 1
            idx_finish -= 1
            continue
        if p[idx_start] == p[idx_finish]:
            idx_start += 1
            idx_finish -= 1
            continue
        return False
    return True


def is_palindrome_from_book_1(p):
    return p == p[::-1]


# print(is_palindrome('казак'))
# print(is_palindrome('Я не стар, брат Сеня!'))

test_string = 'Я не стар, брат Сеня!'

print(timeit.timeit(lambda: is_palindrome(test_string), number=1000000))
print(timeit.timeit(lambda: is_palindrome_from_book_1(test_string), number=1000000))

