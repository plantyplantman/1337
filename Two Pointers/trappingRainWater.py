# https://leetcode.com/problems/trapping-rain-water/

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """

    left, right = 0,  len(height) - 1
    left_max, right_max = height[left], height[right]
    res = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            res += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            res += right_max - height[right]

    return res


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    trapped = trap(height)
    assert trapped == 6
