def _merge(left, right):
    """
    Function merges left and right parts
    Args:
        left: left part of array
        right: right part of array
    Returns:
        Sorted and merged left + right parts
    """

    merge_result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge_result += [left[i]]
            i += 1
        else:
            merge_result += [right[j]]
            j += 1
    merge_result += left[i:len(left)]
    merge_result += right[j:len(right)]

    return merge_result


def merge_sort(array):
    """
    Sort array via merge sort algorithm
    Args:
        array: list of elements to be sorted
    Returns:
        Sorted list of elements
    Examples:
        [-10, 1, 3, 5, 21]
    """
    if len(array) == 1: #if the length of array is 1 return 1
        return array[:]
    mid = len(array) // 2 #else divide the array in 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    sort_result = _merge(left, right)
    return sort_result


print(merge_sort([1, -10, 21, 3, 5]))# array defined in the function itself