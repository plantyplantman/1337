def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    if len(s) != len(t):
        return False

    hashmap = {}
    for i in range(len(s)):
        if s[i] in hashmap:
            hashmap[s[i]] += 1
        else:
            hashmap[s[i]] = 1

        if t[i] in hashmap:
            hashmap[t[i]] -= 1
        else:
            hashmap[t[i]] = -1

    return all(value == 0 for value in hashmap.values())


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
