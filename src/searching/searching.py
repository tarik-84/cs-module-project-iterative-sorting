def linear_search(arr, target):
    # Loop through the array
    for i in range(0, len(arr)):
            if arr[i] == target:
                return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # start = the starting index of the subset of the array we're searching in. inclusive
    # end = the end index of the subset -- inclusive
    start = 0
    end = len(arr) - 1
    while end >= start:
        # Look at the middle
        # how do we get the midpoint?
        # for the whole array, it's len(arr) / 2 - 1
        # for a subset of the array: (start + end) // 2
        middle_index = (start + end) // 2
        middle_value = arr[middle_index]
        # Compare it to the target
        if target == middle_value:
            return middle_index
        if target > middle_value:
            # search the right side
            # set start = middle_index + 1
            start = middle_index + 1
        if target < middle_value:
            # search the left side: set end = middle_index - 1
            end = middle_index - 1
    return -1  # not found
