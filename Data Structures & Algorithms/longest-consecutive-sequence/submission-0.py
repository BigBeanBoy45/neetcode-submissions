class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        tracker: set[int] = set(nums)

        res = 0

        for t in tracker:
            if t - 1 in tracker: 
                continue
            comparator = 1
            while t + comparator in tracker:
                comparator += 1
            if comparator > res: res = comparator
        
        return res

        