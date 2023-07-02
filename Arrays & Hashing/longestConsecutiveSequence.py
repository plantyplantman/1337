# https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    numsSet = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in numsSet:
            x = 1
            while num + x in numsSet:
                x +=1
            longest = max(x, longest)

    return longest


if __name__ == "__main__":
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(longestConsecutive(nums))
