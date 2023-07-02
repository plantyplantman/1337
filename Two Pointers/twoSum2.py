# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    i = 0
    j = len(numbers) - 1

    while i < j:
        if numbers[i] + numbers[j] == target:
            return [i + 1, j + 1]
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(twoSum(numbers, target))

    numbers = [2, 3, 4]
    target = 6
