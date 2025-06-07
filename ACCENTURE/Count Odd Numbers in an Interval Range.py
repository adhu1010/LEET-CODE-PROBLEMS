class Solution (object):
    def countOdds(self, low: int, high: int) -> int:
        """
        Count the number of odd integers in the inclusive range [low, high].

        :param low: The lower bound of the range.
        :param high: The upper bound of the range.
        :return: The count of odd integers in the range.
        """
        return (high + 1) // 2 - low // 2
    
    