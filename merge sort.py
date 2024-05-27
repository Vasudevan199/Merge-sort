def mergeArrays(arr1, arr2, arr3):
    i = 0
    j = 0
    k = 0
    m = len(arr1)
    n = len(arr2)

    # Merge both arrays into arr3 in sorted order
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1

    # Copy any remaining elements of arr1
    while i < m:
        arr3[k] = arr1[i]
        i += 1
        k += 1

    # Copy any remaining elements of arr2
    while j < n:
        arr3[k] = arr2[j]
        j += 1
        k += 1

# Driver code
if __name__ == '__main__':
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]
    arr3 = [0 for _ in range(len(arr1) + len(arr2))]
    
    mergeArrays(arr1, arr2, arr3)
    
    print("Array after merging:")
    for i in range(len(arr3)):
        print(arr3[i], end=" ")
