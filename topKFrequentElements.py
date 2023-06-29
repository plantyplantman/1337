# https://leetcode.com/problems/top-k-frequent-elements/
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    hmap = {}
    for num in nums:
        if num in hmap:
            hmap[num] += 1
        else:
            hmap[num] = 1

    sorted_tuples = sorted(hmap.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_tuples[:k]]
