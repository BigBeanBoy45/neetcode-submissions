class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # SOLUTION WITHOUT DIVISION OPERATION

        length = len(nums)

        # USE PREFIX/SUFFIX APPROACH
        l: list[int] = [1] * length
        r: list[int] = [1] * length
        
        # left multiplies all values to the left of index
        # right " " right of index

        
        # build auxiliary data
        for i in range(length - 1):
            # populate left 
            j = i + 1
            l[j] = nums[i] * l[i]

            # populate right
            k = -(j + 1)
            r[k] = nums[-j] * r[-j]

        # build solution
        res: list[int] = [1] * length
        res[0] = r[0]
        res[-1] = l[-1]
        for i in range(length - 1):
            j = i + 1
            res[j] = l[j] * r[j]
        
        return res