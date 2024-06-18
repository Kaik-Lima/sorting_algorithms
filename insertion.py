def insertion_sort(array):
  # Starting at second element and to go to last element
  for i in range(1, len(array)):
    # Save present element
    key = array[i]
    # Past element index
    j = i - 1
    while j >= 0 and array[j] > key:
      array[j+1] = array[j]
      j -= 1
    # Put the key in correct position
    array[j + 1] = key
  return array


array_order = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(array_order))