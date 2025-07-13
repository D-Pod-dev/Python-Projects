from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            num = nums[i]
            check = nums[i+1:]
            addend = target - num
            if (target - nums[i]) in nums[i+1:]:
                i_num = i
                i_addend = check.index(addend) + i+1
                return [i, nums[i+1:].index(target - nums[i]) + i+1]


print(Solution().twoSum([2,7,11,15], 9))
