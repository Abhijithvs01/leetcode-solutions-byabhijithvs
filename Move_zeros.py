"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""


class Solution(object):
    def moveZeroes(self, nums):
        zero_indices = []
        for i in range (len(nums)):
            if nums[i] == 0:
                zero_indices.append(i)
        for i in reversed(zero_indices):
            nums.pop(i)
        for _ in range(len(zero_indices)):
            nums.append(0)

        return nums