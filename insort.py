a = [12, 5, 3, 7, 5, 11, 7, 9, 34]
for i in range(0, len(a), 1):
    j = i
    while j > 0 and a[j] < a[j - 1]:
        a[j - 1], a[j] = a[j], a[j - 1]
        j -= 1
print(a)
