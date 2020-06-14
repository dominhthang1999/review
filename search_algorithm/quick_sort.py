def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if (arr[j] < pivot):
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], pivot = pivot, arr[i + 1]
    return i + 1

def partition_middle(arr, low, high):

    i = low
    j = high
    pivot = arr[(low + high) // 2]

    while i <= j:
        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1
        if (i <= j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i

def quick_sort_last_pivot(arr, low, high):
    if (low < high):
        pi = partition_middle(arr, low, high)
        quick_sort_last_pivot(arr, low, pi - 1)
        quick_sort_last_pivot(arr, pi , high)


arr = [1, 12, 5, 26, 7, 14, 3, 7, 2]
quick_sort_last_pivot(arr, 0, len(arr) - 1)
print(arr)
