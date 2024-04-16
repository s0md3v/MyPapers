This is a polynomial-time algorithm to solve the Subset Sum Problem.

Below is a rough description of how the algorithm works. It is not comprehensive and is only being added to be added to help with initial peer-review and a proof of invention.

1. Given subset: S
2. Target sum: T
3. Sort the subset S in increasing order.
4. Remove any numbers that are greater than T.
5. Iterate over S in a decreasing order while adding the iterated numbers until we get a sum greater than T. The length of subset formed until this point is N i.e. the minimum possible length of the solution subset.
   5.1 If we iterate through S without the sum becoming greater than T, a solution doesn't exist i.e. even the sum of the entire set is less than T.
4. Iterate over S in an increasing order while adding the iterated numbers until we get a sum greater than T. The length of subset formed until this point is M i..e the maximum possible length of the solution subset.
5. For each number in the set, store its digital root and last digit into memory, lets call this database "mapping".
6. Consider the last N digits of the set. It acts like a set/buffer and its position is from reverse(S) to reverse(S)-N.
   6.1 If the sum of the buffer is greater than T, move to left i.e. to smaller numbers in set.
   6.2 If its sum is equal to T, we have found our solution.
   6.3 If its sum is less than T, proceed with further calculations defined in 7.
7. Lets call the sum of this buffer, BS.
   7.1 Find the digital root of this BS, and calculate what digital(s) root should be added to it to make it equal to the digital root of T.
   7.2. Calculate what digit(s) should be added to it to make the last digit of their sum equal to the last digit of T.
   7.3. Use the information accquired to find the respective set of numbers in the mapping and proceed to 8.
8. Add the first (smallest) number from the accquired set to the sum of buffer.
   8.1 If this sum is equal to T, we have found our solution.
   8.2 If this sum is greater than T, reject this set altogether and go back to 6, and move the buffer one number to the left. This is done because if this number is causing the buffer to be greater than T, the rest of the numbers will do too as they are in increasing order.
   8.2. If this sum is less than then T, reject this number and move to the next number in set.
   8.3. If the end of this accquired set is reached, increase N by 1 and go back to 6.
9. Keep repeating steps 6 to 8 until a solution is found or length of buffer reaches M.
