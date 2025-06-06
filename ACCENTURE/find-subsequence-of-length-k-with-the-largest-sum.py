def maxSubsequence(nums, k):
   
    indexed = [(val, idx) for idx, val in enumerate(nums)]

   
    top_k = sorted(indexed, key=lambda x: -x[0])[:k]

    
    top_k_sorted = sorted(top_k, key=lambda x: x[1])

   
    return [val for val, idx in top_k_sorted]
