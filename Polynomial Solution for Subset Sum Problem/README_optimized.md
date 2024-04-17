This is a polynomial-time algorithm to solve the Subset Sum Problem. It uses calculations based on digital root and last digit of the target sum to reduce the time complexity by never considering "unfit" numbers for a sum.

To test it, add `print(find_solution(18, [1, 6, 6, 4, 5, 12, 15, 21, 53]))` at the end of algorithm_optimized.py file and then run it. If you want to benchmark the time-taken for very large input values, you can do something like:
```python
import random, time
required_sum = 117653409467538
array = random.sample(range(1, 500000000), 50000000) # generate 50000000 random numbers between 1 and 499999999
start = time.time()
solution = find_solution(required_sum, array)
print(solution)
print("seconds taken:", time.time() - start)
```

Below is a rough description of how the algorithm works. It is not comprehensive (or final) and has only been added to help with initial peer-review and as a proof of invention.

```
Given set of positive integers: S
Target sum: T
Problem: Find a subset of S (if it exists) such that its sum is equal to T.

1. Sort the set S in increasing order.
2. Remove any numbers that are greater than T. Adding anything to them will only result in number larger than T.
3. Iterate over S in a decreasing order while adding the iterated numbers until we get a sum greater than T. The length of subset formed until this point is N i.e. the minimum possible length of the solution subset.
   3.1 If we iterate through S without the sum becoming greater than T, a solution doesn't exist i.e. even the sum of the entire set is less than T.
4. Iterate over S in an increasing order while adding the iterated numbers until we get a sum greater than T. The length of subset formed until this point is M i.e. the maximum possible length of the solution subset.
5. For each number in the set, store its digital root and last digit into memory, lets call this database "mapping".
6. Consider the last N digits of the set. It acts like a buffer (dynamic subset) and its position is from reverse(S) to reverse(S)-N.
   6.1 If the sum of the buffer is greater than T, move to left i.e. to smaller numbers in set.
   6.2 If its sum is equal to T, we have found our solution.
   6.3 If its sum is less than T, proceed to 7.
7. Lets call the sum of this buffer, BS.
   7.1 Find the digital root of this BS, and calculate what digital root should be added to it to make it equal to the digital root of T.
   7.2 Calculate what digit should be added to it to make the last digit of their sum equal to the last digit of T.
   7.3 Use the information accquired to find the respective subset of numbers in the mapping, call this subset AS and proceed to 8.
8. Add the first (smallest) number from AS to the sum of buffer.
   8.1 If this sum is equal to T, we have found our solution.
   8.2 If this sum is greater than T, reject AS altogether and go back to 6, and move the buffer one number to the left. This is done because if this number is causing the buffer to be greater than T, the rest of the numbers will do too as they are in increasing order.
   8.2 If this sum is less than then T, reject this number and move to the next number in AS.
   8.3 If all the numbers in AS resultsed in a sum less than T, increase N by 1 and go back to 6. This is done because if all sums for the N-1 largest numbers isn't big enough, the rest of S is only smaller because we are iterating bigges->smallest.
   8.4 If the end of this accquired set is reached, increase N by 1 and go back to 6.
9. Keep repeating steps 6 to 8 until a solution is found or length of buffer reaches M.
```
