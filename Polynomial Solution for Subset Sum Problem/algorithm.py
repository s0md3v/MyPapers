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


def process_buffer(seed_buffer, mapping, req_sum, req_root, req_last, indexes):
    """
    Process the buffer to find a sequence of numbers that meet the requirements.
    
    Parameters:
    seed_buffer (list): The number sequence.
    req_sum (int): The required sum.
    req_root (int): The required digital root.
    req_last (int): The required last digit.
    indexes (dict): The indexes for mapping.

    Returns:
    list: The sequence of numbers that meet the requirements.
    """
    buffer, buffer_sum = [], 0
    good_buffers = [(seed_buffer, sum(seed_buffer))]
    previous_cords = [0, 0]
    for_root, for_last = 0, 0
    while good_buffers:
        buffer, buffer_sum = good_buffers.pop()
        for_root = root_map[(buffer_sum - 1) % 9 + 1][req_root]
        for_last = (req_last - buffer_sum % 10) % 10
        this_array = mapping[for_root][for_last]
        if not this_array:
            break
        index = indexes[for_root][for_last]
        i = this_array[index]
        if buffer_sum + i >= req_sum:
            if buffer_sum + i == req_sum:
                return buffer + [i]
            break
        elif index + 1 <= len(this_array) - 1:
            if buffer_sum + this_array[index+1] <= req_sum:
                if previous_cords != [for_root, for_last]:
                    good_buffers.append((buffer + [this_array[index+1]],buffer_sum + this_array[index+1]))
                    indexes[for_root][for_last] += 1
                previous_cords = [for_root, for_last]
    return []


def start_growing(array, mapping, req_sum, req_root, req_last, start, end, end_with):
    """
    Grow the buffer until 'end' to find a subset of numbers that sum to req_sum.
    
    Parameters:
    array (list): The number set.
    req_sum (int): The required sum.
    start (int): The initial length of the buffer.
    end (int): The maximum length for the buffer.
    end_with (int): The end index for the buffer.
    req_root (int): The required digital root.
    req_last (int): The required last digit.

    Returns:
    list: The subset of numbers that meet the requirements.
    """
    steps = 1
    buffer_end = min(end_with, len(array))
    buffer_start = buffer_end - start - steps
    running_total = sum(array[buffer_start:buffer_end])
    indexes_reset = {i: {j: 0 for j in range(10)} for i in range(1, 10)}
    while buffer_end - buffer_start <= end:
        buffer = array[buffer_start:buffer_end]
        if running_total <= req_sum:
            if running_total == req_sum:
                return buffer
            indexes = indexes_reset
            result = process_buffer(buffer, mapping, req_sum, req_root, req_last, indexes)
            if result:
                return result
        if not buffer:
            steps += 1
            buffer_end = min(end_with - steps, len(array))
            buffer_start = buffer_end - (start + steps)
            buffer = array[buffer_start:buffer_end]
            if not buffer:
                break
            continue
        running_total -= array[buffer_end-1]
        buffer_start -= 1
        buffer_end -= 1
        if buffer_start >= 0:
            running_total += array[buffer_start]
    return []


def find_solution(required_sum, array):
    """
    Find a solution that meets the requirements.
    
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

    end = 0 # maximum possible length of the solution subset
    this_sum = 0

    for index, i in enumerate(reversed(array)):
        this_sum += i
        if this_sum > required_sum:
            if index == 0:
                end = 2
            end = 2 if index - 1 <= 1 else index - 1 
            break
        return [] # the sum of entire set is less than required_sum, solution doesn't exist

    start = 0 # minimum possible length of the solution subset
    this_sum = 0
    for index, i in enumerate(array):
        this_sum += i
        if this_sum > required_sum:
            end = index
            break

    # mapping of each number in the set to its digital root and last digit
    mapping = {i: {j: [] for j in range(10)} for i in range(1, 10)}

    for i in array:
        this_sum = (i - 1) % 9 + 1 # digital root, used throughout the algorithm
        req_last = i % 10
        mapping[this_sum][req_last].append(i)

    req_root, req_last = (required_sum - 1) % 9 + 1, required_sum % 10
    return start_growing(array, mapping, required_sum, req_root, req_last, start, end, len(array))