def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if (arr[j] < pivot):
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], pivot = pivot, arr[i + 1]
    return i + 1

def quick_sort_last_pivot(arr, low, high):
    if(low < high):
        pi = partition(arr, low, high)
        quick_sort_last_pivot(arr, low, pi - 1)
        quick_sort_last_pivot(arr, pi + 1, high)

arr = [10, 80, 30, 90, 40, 50, 70 ]
quick_sort_last_pivot(arr, 0, len(arr) - 1)
print(arr)