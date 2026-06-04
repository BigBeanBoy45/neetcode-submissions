class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # two-pointer greedy
        # area = (left_index - right_index) * min(left_height, right_height)
        
        res: int = -1

        l: int = 0
        r: int = len(heights) - 1

        def getArea(left: int, right: int, width) -> int:
            return min(left, right) * width

        while l < r:
            left: int = heights[l]
            right: int = heights[r]    
            left_lesser: bool = True if left < right else False        
            # keep track of min side: T for left, F for right
            area: int = getArea(left, right, r-l)
            
            res = max(res, area)

            if left_lesser: 
                l += 1 
            else: 
                r -= 1


        return res