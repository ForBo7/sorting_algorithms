my_list = [25, 34, 98, 7, 41, 19, 5]
stopping_index = len(my_list) - 1

# Outer loop so that we go through each element in the list.
for x in range(len(my_list)):
    for current_index in range(stopping_index):
        if my_list[current_index] > my_list[current_index+1]:
            # Swap values.
            temp = my_list[current_index]
            my_list[current_index] = my_list[current_index+1]
            my_list[current_index+1] = temp
    # So that we don't compare the already sorted values.
    stopping_index -= 1

print(my_list)
