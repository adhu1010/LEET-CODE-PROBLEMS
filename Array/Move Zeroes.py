class Move_zeroes:
    def move_zeroes(self,nums):
        insert_position=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[insert_position]=nums[i]
                insert_position+=1
        while insert_position<len(nums):
            nums[insert_position]=0
            insert_position+=1
        return nums
nums = [0, 1, 0, 3, 12]
solution = Move_zeroes()
print(solution.move_zeroes(nums))