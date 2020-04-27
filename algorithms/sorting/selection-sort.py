from typing import List

def selection_sort(num_list: List[int]) -> List[int]:
    # initialize current_sorted_index
    current_sorted_index = 0
    # while current_sorted_index < len(num_list)
    while current_sorted_index < len(num_list):
        # init smallest_num 
        smallest_num_index = current_sorted_index
        # for i in range(current_sorted_index, len(num_list))
        for index in range(current_sorted_index, len(num_list)):
            # check if num_list[i] < smallest_num
            if num_list[index] < num_list[smallest_num_index]:
                smallest_num_index = index
        
        num_list[current_sorted_index], num_list[smallest_num_index] = num_list[smallest_num_index], num_list[current_sorted_index] 

        current_sorted_index += 1

    return num_list

test_list = [5, 3, 9, 1, 70, 0, 3, 8, 3, 54, 12]

print(selection_sort(test_list))