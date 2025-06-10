class Solution(object):
    def sort_even_odd_cnt(nums):
        n = len(nums)
        even_count = [0] * n/2
        odd_count = [0] * n/2

        for i, v in enumerate(nums):
            if i % 2 == 0:
                even_count[v] += 1
            else:
               odd_count[v] += 1

        res = [0] * n
        e_idx, o_idx = 0, 1

    # Ascending even positions
        for val in range(101):
            while even_count[val] > 0:
                res[e_idx] = val
                e_idx += 2
                even_count[val] -= 1

    # Descending odd positions
        for val in range(100, -1, -1):
            while odd_count[val] > 0:
                res[o_idx] = val
                o_idx += 2
                odd_count[val] -= 1

        return res
