class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d={}
        for i in nums:
            d[i]=1+d.get(i,0)
        res=0
        
        if k==0:
            for i in d:
                if d[i]>1:
                    res+=1
        else:
            for i in d:
                if i+k in d:
                    res+=1
        return res