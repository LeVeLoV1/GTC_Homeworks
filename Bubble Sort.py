arr = [12, 5, 3, 7, 5, 9, 11, 6, 17, 2]


def bubble_Sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


bubble_Sort(arr)
