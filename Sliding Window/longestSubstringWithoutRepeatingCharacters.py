# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "":
        return 0
    retv = 1

    for i, c in enumerate(s):
        seen = set()
        seen.add(c)
        j = i + 1
        if j < len(s):
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                j += 1
        retv = max(j-i, retv)

    return retv
