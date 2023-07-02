# https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """

    l = 0
    r = len(height) - 1
    max_area = 0

    while l < r:
        length = r - l
        area = length * min(height[l], height[r])
        max_area = max(max_area, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    maxArea = maxArea(height)
    assert maxArea == 49
