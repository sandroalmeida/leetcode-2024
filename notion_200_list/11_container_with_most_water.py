def maxArea(height):
    l, r = 0, len(height) - 1
    res = 0
    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return res


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))