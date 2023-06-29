# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    hmap = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        hmap[tuple(count)].append(word)

    return hmap.values()
