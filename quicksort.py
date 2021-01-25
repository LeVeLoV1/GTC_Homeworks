a = [10, 3, 3, 55, 7, 6, 45, 12]


def quick_sort(l, r):
    i = l
    j = r
    k = a[(l + r) // 2]
    while i <= j:
        while a[i] < k:
            i += 1
        while a[j] > k:
            j += 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
    if i < j:
        quick_sort(l, j)
    if i < r:
        quick_sort(l, r)
    return a


print(quick_sort(0, len(a) - 1))
