def maxSubsequence(nums, k):
   
    indexed = [(val, idx) for idx, val in enumerate(nums)]

   
    top_k = sorted(indexed, key=lambda x: -x[0])[:k]

    
    top_k_sorted = sorted(top_k, key=lambda x: x[1])

   
    return [val for val, idx in top_k_sorted]
#Program Explanation
"""To maximize the sum, we need the k largest elements from the array.

We store each element along with its original index as (value, index).

Sort these pairs by value (in descending order) and select the top k.

Now sort these k elements by their original index to preserve order.

Extract only the values from the sorted pairs.

This ensures the result is a valid subsequence with the maximum sum.

Return this final list of k values. """