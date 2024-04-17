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

    array_length = len(array)
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
            temp_small = True
            for i in array:
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
