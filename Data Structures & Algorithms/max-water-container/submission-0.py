class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # area = (left_index - right_index) * min(left_height, right_height)

        res: int = -1
        length: int = len(heights)
        for i in range(length):
            left: int = heights[i]
            j: int = i + 1
            while j < length:
                right: int = heights[j]
                area: int = (j - i) * min(left, right)
                if area > res: 
                    res = area
                j += 1

        return res