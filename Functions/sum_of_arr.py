def sum_array(arr):
    if arr:
        arr.remove(min(arr))
        if arr:
            arr.remove(max(arr))
        return sum(arr)
    return 0
