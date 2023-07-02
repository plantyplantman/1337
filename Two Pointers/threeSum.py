# https://leetcode.com/problems/3sum/

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    nums = sorted(nums)

    result = []

    for (i, a) in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            _sum = a + nums[left] + nums[right]
            if _sum > 0:
                right -= 1
            elif _sum < 0:
                left += 1
            else:
                result.append([a, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
