class Solution(object):
    def twoSum(self, nums, target):
        num_index_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_index_map:
                return [num_index_map[complement], index]
            num_index_map[num] = index
        return None  