def selection_sort(array):
  for i in range(len(array)):
    min = i
    for j in range(i + 1, len(array)):
      if array[j] < array[min]: min = j
    # Replace the smaller element with the first element
    array[i], array[min] = array[min], array[i]
  return array


array_order = [64, 34, 25, 12, 22, 11, 90]
selection_sort(array_order)