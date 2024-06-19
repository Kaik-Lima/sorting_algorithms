def quick_sort(array):
    def cut(array, bottom, upper):
        pivot = array[upper]
        # smaller element index
        i = bottom - 1
        for j in range(bottom, upper):
            if array[j] <= pivot:
                i += 1
                # replacement the elements
                array[i], array[j] = array[j], array[i]
        # replace the pivot for correct position 
        array[i+1], array[upper] = array[upper], array[i+1]
        return i + 1
    
    # Main recursive function of Quick Sort
    def quick_sort_recursive(array, bottom, upper):
        if bottom < upper:
            pi = cut(array, bottom, upper)
            quick_sort_recursive(array, bottom, pi - 1)
            quick_sort_recursive(array, pi + 1, upper)
    # initial call of recursive function
    quick_sort_recursive(array, 0, len(array) - 1)
    return array


array_order = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(array_order))