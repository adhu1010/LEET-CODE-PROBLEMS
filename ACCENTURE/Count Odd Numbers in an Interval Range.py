class Solution (object):
    def countOdds(self, low: int, high: int) -> int:
        """
        Count the number of odd integers in the inclusive range [low, high].

        :param low: The lower bound of the range.
        :param high: The upper bound of the range.
        :return: The count of odd integers in the range.
        """
        return (high + 1) // 2 - low // 2
    
    """Program Explanation
    The task is to count the number of odd integers in the inclusive range [low, high].
    - If `low` is odd, it contributes one odd number.
    - If `high` is odd, it contributes one odd number.
    - The total count of odd numbers can be calculated by:
      - Adding 1 if `low` is odd.
      - Adding 1 if `high` is odd.
      - The formula `(high + 1) // 2 - low // 2` effectively counts the odd numbers in the range."""