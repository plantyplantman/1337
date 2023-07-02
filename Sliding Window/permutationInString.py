# https://leetcode.com/problems/permutation-in-string/

def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if len(s1) > len(s2):
        return False

    s1count = [0] * 26
    s2count = [0] * 26

    for i in range(len(s1)):
        s1count[ord(s1[i]) - ord('a')] += 1
        s2count[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(len(s1count)):
        matches += 1 if s1count[i] == s2count[i] else 0

    left = 0
    for right in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[right]) - ord('a')
        s2count[index] += 1

        if s1count[index] == s2count[index]:
            matches += 1
        elif s1count[index] + 1 == s2count[index]:
            matches -= 1

        index = ord(s2[left]) - ord('a')
        s2count[index] -= 1
        if s1count[index] == s2count[index]:
            matches += 1
        elif s1count[index] - 1 == s2count[index]:
            matches -= 1

        left += 1
    return matches == 26


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"

    res = checkInclusion(s1, s2)
    assert res == True
