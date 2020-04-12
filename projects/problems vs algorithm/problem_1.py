def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Handle non-integer inputs
    try:
        int(number)
    except ValueError:
        return None
    # Handle negative integer
    if number < 0:
        return None

    # Handle zero value
    if number <= 1:
        return number
    lowest, highest = 2, number // 2

    while lowest <= highest:
        candidate = ((highest - lowest) // 2) + lowest
        sq_candidate = candidate * candidate

        if sq_candidate == number:
            return candidate

        if sq_candidate > number:
            highest = candidate - 1
        else:
            # If the next largest number squared is greater than the target, return the current candidate
            sq_candidate_plus = (candidate + 1) * (candidate + 1)
            if sq_candidate_plus > number:
                return candidate
            lowest = candidate + 1
     # If we got this far, all hope is lost
    return None
    

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (None == sqrt(-5)) else "Fail")
print ("Pass" if  (None == sqrt('sa')) else "Fail")
print ("Pass" if  (None == sqrt(3)) else "Fail")