class Solution(object):
    def sortEvenOdd(self, num):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(num)):
            for index in range(0,len(num)-i-1):
                if  (index)%2==0:
                    if (index+2)<(len(num)) and num[index]>num[index+2]:
                        num[index],num[index+2]=num[index+2],num[index]
                else:
                    if (index+2)<(len(num)) and num[index]<num[index+2]:
                        num[index],num[index+2]=num[index+2],num[index]
            
        return num
    

nums = [36,45,32,31,15,41,9,46,36,6,15,16,33,26,27,31,44,34]
solution = Solution()
sorted_nums = solution.sortEvenOdd(nums)
print(sorted_nums)
Output= [9,46,15,45,15,41,27,34,32,31,33,31,36,26,36,16,44,6]
if sorted_nums==Output:
    print("Output is correct")  