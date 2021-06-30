def improved_bubble_sort(list):
    """
    Does a bubble sort in ascending order on the provided list.
    Algorithm halts if list is already sorted.
    """
    stopping_index = len(list) - 1
    # Variable to check whether any swaps have happened.
    any_swaps = True
    # Outer loop so that we go through each element in the list.
    while any_swaps:
        any_swaps = False
        for current_index in range(stopping_index):
            if list[current_index] > list[current_index + 1]:
                # Swap values.
                temp = list[current_index]
                list[current_index] = list[current_index + 1]
                list[current_index + 1] = temp
                any_swaps = True
        # So that we don't compare the already sorted values.
        stopping_index -= 1
