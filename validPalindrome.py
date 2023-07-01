# https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    j = len(s) - 1

    for i, c in enumerate(s):
        if j < i:
            return True
        if not c.isalnum():
            continue
        # print(f"i: {i}, c: {c}, j: {j}, s[j]: {s[j]}")
        while j > i and not s[j].isalnum():
            j -= 1

        if c.upper() != s[j].upper():
            return False
        else:
            j -= 1

    return True


if __name__ == "__main__":
    s1 = "A man, a plan, a canal: Panama"
    print(isPalindrome(s1))

    s2 = "race a car"
    print(isPalindrome(s2))

    s3 = "0P"
    print(isPalindrome(s3))

    s4 = " "

    print(isPalindrome(s4))