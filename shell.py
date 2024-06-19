def shell_sort(array):
    n = len(array)
    interval = n // 2
    # Divide interval until it equals 0
    while interval > 0:
        for i in range(interval, n):
            # Save current value
            mark = array[i]
            j = i
            while j >= interval and array[j - interval] > mark:
                array[j] = array[j - interval]
                j -= interval
            # Inserting the saved value in correct position
                array[j] = mark
        # Divide for half
        interval //= 2
    return array


array_order = [64, 34, 25, 12, 22, 11, 90]
print(shell_sort(array_order))