def insertion_sort(list):
    """Performs an insertion sort on the provided list."""

    for unsorted_pointer in range(1, len(list)):
        # Item to sort.
        current_element = list[unsorted_pointer]

        sorted_pointer = unsorted_pointer - 1
        while current_element < list[sorted_pointer]:
            list[sorted_pointer+1] = list[sorted_pointer]
            sorted_pointer -= 1

            # Insert current_element at the beginning of the list.
            #  Meaning that the value of current_element is the smallest
            #  value yet.
            if sorted_pointer == -1:
                list[0] = current_element
                break
        list[sorted_pointer+1] = current_element
