def count_k(a: list, k: int):
    def rcount(lo, hi):
        """Основание рекурсии:
        Если длина списка четная и lo > hi то возвращаем 0
        Если длина списка нечетная и lo == hi то проверяем, равен ли этот элемент k

        Рекурсивный случай:
        Обходим массив с двух сторон, пока не дойдем до середины
        Если какое-то значение равно k, увеличиваем счетчик
        """
        if len(a) % 2 != 0 and lo == hi:
            return 1 if a[0] == k else 0
        elif len(a) % 2 == 0 and lo > hi:
            return 0

        cnt = 0
        if a[lo] == k:
            # print(f'{a[lo]=}')
            cnt += 1
        if a[hi] == k:
            # print(f'{a[hi]=}')
            cnt += 1
        # print(f'{lo=}, {hi=}, {cnt=}')
        return cnt + rcount(lo+1, hi-1)
    return rcount(0, len(a)-1)


print(count_k([5, 9, 0, 4, 4, 4, 6, 8, 3, 4, 4, 4, 4], 4))
