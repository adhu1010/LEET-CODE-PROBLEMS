class Solution(object):
    def pathSum(self, nums):
        tree = {}
        for num in nums:
            d, p, v = num // 100, (num // 10) % 10, num % 10
            tree[(d, p)] = v

        self.total = 0

        def dfs(d, p, running_sum):
            if (d, p) not in tree:
                return

            running_sum += tree[(d, p)]

            left = (d + 1, p * 2 - 1)
            right = (d + 1, p * 2)

            if left not in tree and right not in tree:
                # It's a leaf
                self.total += running_sum
            else:
                dfs(d + 1, p * 2 - 1, running_sum)
                dfs(d + 1, p * 2, running_sum)

        dfs(1, 1, 0)
        return self.total

# Time Complexity: O(n) where n is the number of elements in nums, as we traverse each element once.
# Space Complexity: O(n) for storing the tree structure in a dictionary.