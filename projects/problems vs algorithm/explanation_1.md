# Finding the square root of an integer #
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:

## Details ##
Given a target number, `number`, the `sqrt` function first checks for the edges cases where `target` is 0 or 1 or not integer at all.

The function then determines the lowest possible square root, and the highest possible square root. It assigns these values to the variables `lowest` and `highest`.

As we've already handled the 0 and 1 edge cases, the initial value of `lowest` is 2. The initial value of `highest` is `target // 2` (as we're only interested in an integer result).

The binary search is implemented using a loop. The loop continues until `lowest` is greater than `highest`. For each loop iteration, we do the following:

1. Determine the halfway point (as an integer) between `lowest` and `highest`. Assign this value to the variable `candidate`.
2. Determine whether `candidate * candidate` is equal to `target`. If so, return `candidate`.
3. Determine whether `candidate * candidate` is greater than `target`. If so, update `highest` to be `candidate - 1`. This discards the "top half" of possible values. Continue with the next loop iteration.
4. Determine whether `(candidate + 1) * (candidate + 1)` is _more than_ `target`. If so, return `candidate`.
5. Update `lowest` to be `candidate + 1`. This discards the "bottom half" of possible values. Continue with the next loop iteration.

If the loop completes without finding a suitable candidate, the function returns `None`.

## Efficiency ##

### Time efficiency ###
The time efficiency of binary search (and therefore this solution) is `O(log(n))`. This matches the expected time complexity stated in the problem description.

### Space efficiency ###
The space efficiency of this solution is `O(1)`. No temporary data structures are used in order to arrive at the solution.