class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = 0
        for index,value in enumerate(prices):
            for max in prices[index+1:]:
                if max>value:
                    diff=max(diff,max-value)
        return diff
    
p=[7,1,5,3,6,4]
a=Solution()
b=a.maxProfit(p)
print(b)