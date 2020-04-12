
def get_min_max_by_sorting(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return
    #      maximum         minimum
    sol = [-float('inf'), float('inf')]
    for num in ints:
        if num > sol[0]:
            sol[0] = num
        if num < sol[1]:
            sol[1] = num
    return (sol[1], sol[0])

## Example Test Case of Ten Integers
import random

randomList = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(randomList)

print ("Pass" if ((-1, 9) == get_min_max_by_sorting([1,1,0,5,9,-1])) else "Fail")
print ("Pass" if ((0, 0) == get_min_max_by_sorting([0])) else "Fail")
print ("Pass" if (None == get_min_max_by_sorting([])) else "Fail")
print ("Pass" if ((0, 9) == get_min_max_by_sorting(randomList)) else "Fail")