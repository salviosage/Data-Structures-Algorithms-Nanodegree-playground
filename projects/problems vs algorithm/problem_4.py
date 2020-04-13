def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    freq = [0] * 3
    for number in input_list:
        freq[number] += 1
    input_list = []
    for i in range(3):
        input_list.extend([i]*freq[i])
    return input_list


    
def sort_013(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    current_i = 0
    left_i = 0
    last_i = len(input_list) - 1
    while current_i <= last_i:
        if input_list[current_i] is 2:
            input_list[last_i],input_list[current_i]=input_list[current_i],input_list[last_i]
            last_i-=1
            continue
        if input_list[current_i] is 0:
            input_list[current_i], input_list[left_i] = input_list[left_i], input_list[current_i]
            left_i+= 1

        current_i += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_013(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 2, 2, 1, 1, 1, 2, 2])
test_function([])
test_function([0, 0, 0])