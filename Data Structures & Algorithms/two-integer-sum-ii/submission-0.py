class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointer approach
        # guaranteed valid solution

        i: int = 0
        j: int = len(numbers) - 1

        while True:
            
            combine: int = numbers[i] + numbers[j]

            if combine > target:
                j -= 1
            elif combine < target: 
                i += 1
            else:
                break

        return list([i+1, j+1])