# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    set_nums = set(nums)
    if len(set_nums) == len(nums):
        return False
    else:
        return True
