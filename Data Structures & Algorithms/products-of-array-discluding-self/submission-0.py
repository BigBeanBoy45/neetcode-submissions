class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # SOLUTION WITH DIVISION OPERATION
        # EXPLICITLY HANDLE ZEROS

        length: int = len(nums)

        # CORNER CASE WHERE ONLY ZEROS EXIST IN SOLUTION
        if nums.count(0) >= 2:
            return [0] * length
        # END 2X 0

        # CORNER CASE ONE NON-ZERO EXISTS IN SOLUTION
        if nums.count(0) == 1:
            res = [0] * length
            total_product = 1
            zero_index: int = 0
            
            for i in range(length):
                n = nums[i]
                if n == 0:
                    zero_index = i
                    continue
                total_product *= n
            res[zero_index] = total_product
            return res
        # END 1X 0 


        # DEFAULT CASE

        # build group product
        total_product: int = 1
        for n in nums: total_product *= n

        # build output 
        res: list[int] = [total_product] * length

        # chip away at values to get result
        for i in range(length): res[i] = int(res[i] / nums[i])

        return res