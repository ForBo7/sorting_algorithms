def bubble_sort(list):
    """Does a bubble sort in ascending order on the provided list."""
    stopping_index = len(list) - 1
    # Outer loop so that we go through each element in the list.
    for x in range(len(list)):
        for current_index in range(stopping_index):
            if list[current_index] > list[current_index + 1]:
                # Swap values.
                temp = list[current_index]
                list[current_index] = list[current_index + 1]
                list[current_index + 1] = temp
        # So that we don't compare the already sorted values.
        stopping_index -= 1
