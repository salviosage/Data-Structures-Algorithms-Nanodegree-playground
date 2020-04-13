def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    l = len(input_list)
    if l <= 1:
        return [-1, -1]

    input_freq = [0] * 10
    for num in input_list:
        input_freq[num] += 1

    a1 = []
    a2 = []
    first = 1
    if l % 2 != 0:
        first = 2
    for i in range(9, -1, -1):
        while input_freq[i]:
            if first:
                a1.append(str(i))
                first -= 1
            else:
                first += 1
                a2.append(str(i))
            input_freq[i] -= 1
    return [int(''.join(a1)), int(''.join(a2))]
    

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test case 1 - un-sorted array as input
test_case_1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
# Should print pass as the output should be [964, 852]
test_function(test_case_1)

# Test case 2 - sorted array as input
test_case_2 = [[1, 2, 3, 4, 5], [542, 31]]
# Should print pass as the output should be [542, 31]
test_function(test_case_2)

# Test case 3 - empty array as input
test_case_3 = [[], [-1, -1]]
# Should print pass as the output should be []
test_function(test_case_3)

# Test case 6 - single input list
test_case_6 = [[3], [-1, -1]]
# Should print pass as the output should be [-1, -1] becouse it cant form two number from one number input
test_function(test_case_6)

# Test case 7 - single  number input list
test_case_7 = [[3,0], [3, 0]]
# Should print pass as the output should be [3, 0] becouse its two number input list
test_function(test_case_6)

test_case_4=([[1, 2, 3, 4, 5], [542, 31]])
test_case_5 = [[4, 6, 2, 5, 9, 8], [964, 852]]

test_function(test_case_4)
test_function(test_case_5)