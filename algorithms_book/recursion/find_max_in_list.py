def find_max(a):
    def rmax(lo, hi):
        if lo == hi:
            return a[lo]
        mid = (lo+hi) // 2
        l = rmax(lo, mid)
        r = rmax(mid+1, hi)
        return max(l, r)
    return rmax(0, len(a)-1)


print(find_max([1, 9, 90, 5, 6, -8]))
