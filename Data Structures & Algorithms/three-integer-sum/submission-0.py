class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res: set[tuple[int, int, int]] = set()

        length: int = len(nums)
        nums.sort()

        prev = None
        for i in range(length - 2):
            subtarget: int = -nums[i]
            if prev == subtarget: 
                continue
            # now it's a two sum problem
            tracker: set[int] = set()
            for j in range(i+1, length):
                cursor = nums[j]
                if subtarget - cursor not in tracker:
                    tracker.add(cursor)
                else:
                    res.add((nums[i], subtarget - cursor, cursor))
            prev = subtarget
        
        return list(list(r) for r in res)