# https://leetcode.com/problems/two-sum/
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hmap = {}

    for i, num in enumerate(nums):
        if target - num in hmap:
            return [hmap[target - num], i]
        hmap[num] = i
