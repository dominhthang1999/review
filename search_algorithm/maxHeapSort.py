def heapIfy(arr, n, i):

    largest = i  # root
    L = 2*i + 1
    R = 2*i + 2

    if L < n and arr[L] > arr[largest]:
        largest = L

    if R < n and arr[R] > arr[largest]:
        largest = R

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapIfy(arr, n, largest)

def maxHeapSort(arr):
    lenArr = len(arr)
    # Build heap
    for i in range(lenArr//2 -1, -1, -1):
        heapIfy(arr, lenArr, i)

    for i in range(lenArr - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapIfy(arr, i, 0)

arr = [38, 27, 43, 3, 9, 82, 10]
maxHeapSort(arr)
print(arr)