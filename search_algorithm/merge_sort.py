def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr)//2  #Find middle array
        L = arr[:middle]        # Dividing the array element
        R = arr[middle:]        # into 2 halves

        merge_sort(L)           # Sorting the first haft
        merge_sort(R)           # Sorting the second haft

        i = 0  # index in L
        j = 0  # index in R
        k = 0  # index in arr result

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(arr)
