def merge_sort(array):
  #Checking if the array has more than one element
  if len(array) > 1:
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]
    # Recursively sorts the first half
    merge_sort(left)
    merge_sort(right)
    # Init the index for traverse the two halves
    i = j = k = 0
    # Just two ordered halves
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        array[k] = left[i]
        i += 1
      else:
        array[k] = right[j]
        j += 1
      k += 1

    # Check if there are elements left in the left half
    while i < len(left):
      array[k] = left[i]
      i += 1
      k += 1
    # Check if there are elements left in the right half
    while j < len(right):
      array[k] = right[j]
      j += 1
      k += 1
  return array


array_order = [64, 34, 25, 12, 22, 11, 90]
merge_sort(array_order)