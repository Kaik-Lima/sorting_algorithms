def bubble_sort(array):
  number = len(array)
  for i in range(number):
    for j in range(0, number-i-1):
      # If present element are more, replace the position with the next
      if array[j] > array[j+1]: array[j], array[j+1] = array[j+1], array[j]
  return array


array_order = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(array_order))