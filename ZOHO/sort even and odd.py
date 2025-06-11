def sort_even_odd(nums):
    # Slice out even-indexed and odd-indexed elements
    even_vals = sorted(nums[0::2])
    odd_vals = sorted(nums[1::2], reverse=True)

    # Place them back into a copy (or nums itself)
    result = nums[:]  # or just do nums in-place
    result[0::2] = even_vals
    result[1::2] = odd_vals

    return result
