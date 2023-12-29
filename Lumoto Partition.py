def quicksort_lomuto(arr, start, end):
    if start < end :

        # Partition the array and get the pivot index

        pivot_index = lomuto_partition(arr, start, end)

        # Recursively sort the subarrays on the left and right of the pivot

        quicksort_lomuto(arr, start, pivot_index - 1)
        quicksort_lomuto(arr, pivot_index + 1, end)

def lomuto_partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

# Example usage 
arr = [4, 2, 7, 1, 3] 
print("Original Array:", arr) 
quicksort_lomuto(arr, 0, len(arr) - 1) 
print("Sorted Array:", arr)
