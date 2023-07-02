# https://leetcode.com/problems/longest-repeating-character-replacement/

def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """

    count = {}

    left = 0
    maxf = 0
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)
        maxf = max(maxf, count[s[right]])

        if (right - left + 1) - maxf > k:
            count[s[left]] -= 1
            left += 1

    return (right - left + 1)


if __name__ == "__main__":
    s = "ABAB"
    k = 2
    test1 = characterReplacement(s, k)
    assert test1 == 4

    s = "AABABBA"
    k = 1
    test2 = characterReplacement(s, k)
    assert test2 == 4

    s = "A"
    k = 0
    test3 = characterReplacement(s, k)
    assert test3 == 1

    s = "ABBB"
    k = 2
    test4 = characterReplacement(s, k)
    assert test4 == 4

    s = "ABBCBBBA"
    k = 1
    test5 = characterReplacement(s, k)
    assert test5 == 6
