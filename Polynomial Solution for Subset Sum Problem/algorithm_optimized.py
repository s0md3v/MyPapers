"""
This is a pre-calculated table of digital root calculations.
{current_digital_root: {target_digital_root: digitaL_root_to_add, ...}, ...}
"""

root_map = {
    1: {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 1: 9},
    2: {3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 7, 1: 8, 2: 9},
    3: {4: 1, 5: 2, 6: 3, 7: 4, 8: 5, 9: 6, 1: 7, 2: 8, 3: 9},
    4: {5: 1, 6: 2, 7: 3, 8: 4, 9: 5, 1: 6, 2: 7, 3: 8, 4: 9},
    5: {6: 1, 7: 2, 8: 3, 9: 4, 1: 5, 2: 6, 3: 7, 4: 8, 5: 9},
    6: {7: 1, 8: 2, 9: 3, 1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9},
    7: {8: 1, 9: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9},
    8: {9: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9},
    9: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}}

def find_solution(required_sum, array):
    """
    Find a subset of array that sums to required_sum.
    
    Parameters:
    required_sum (int): The required sum.
    array (list): The number set.

    Returns:
    list: The subset of numbers that meet the requirements.
    """
    array = sorted(array)
    remove_till = 0
    for index, i in enumerate(reversed(array)):
        if i > required_sum:
            remove_till = len(array) - index
        else:
            if remove_till:
                array = array[:remove_till]
            break

    start = 0 # maximum possible length of the solution subset
    this_sum = 0

    for index, i in enumerate(reversed(array)):
        this_sum += i
        if this_sum > required_sum:
            if index == 0:
                start = 2
            start = 2 if index - 1 <= 1 else index - 1 
            break
        start = -1

    if this_sum == required_sum:
        return array
    if start == -1: # if sum of entire set is less than required_sum
        return

    end = 0 # minimum possible length of the solution subset
    this_sum = 0
    for index, i in enumerate(array):
        this_sum += i
        if this_sum > required_sum:
            end = index
            break

    mapping = {i: {j: [] for j in range(10)} for i in range(1, 10)}

    for i in array:
        this_sum = (i - 1) % 9 + 1 # python syntax for finding digital root of i
        req_last = i % 10
        mapping[this_sum][req_last].append(i)

    array_length = len(array)
    req_root, req_last = (required_sum - 1) % 9 + 1, required_sum % 10
    steps = 1
    buffer_end = min(array_length, len(array))
    buffer_start = buffer_end - start - steps
    running_total = sum(array[buffer_start:buffer_end])
    while buffer_end - buffer_start <= end:
        buffer = array[buffer_start:buffer_end]
        all_small = False
        if running_total <= required_sum:
            if running_total == required_sum:
                return buffer
            for_root = root_map[(running_total - 1) % 9 + 1][req_root]
            for_last = (req_last - running_total % 10) % 10
            temp_small = True
            for i in mapping[for_root][for_last]:
                if running_total + i >= required_sum:
                    temp_small = False
                    if running_total + i == required_sum:
                        return buffer + [i]
                    break # only larger numbers are left, no need to continue
            if temp_small: # all_small is True if rest of the numbers are too small for required_sum
                all_small = True
        if not buffer or all_small:
            steps += 1
            buffer_end = min(array_length - steps, len(array))
            buffer_start = buffer_end - (start + steps)
            buffer = array[buffer_start:buffer_end]
            if not buffer: # end of set reached, solution doesn't exist
                break
            continue
        running_total -= array[buffer_end-1]
        buffer_start -= 1
        buffer_end -= 1
        if buffer_start >= 0:
            running_total += array[buffer_start]
