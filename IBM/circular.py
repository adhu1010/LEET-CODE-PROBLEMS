class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
       
        start = rounds[0]
        end = rounds[-1]

        if start <= end:
            return [i for i in range(start, end + 1)]
        else:
            return [i for i in range(1, end + 1)] + [i for i in range(start, n + 1)]