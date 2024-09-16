def trapWithExtraMemory(height):
    maxLeft = [0] * len(height)
    currentMax = 0
    for i, h in enumerate(height):
        maxLeft[i] = currentMax
        if h > currentMax:
            currentMax = h

    maxRight = [0] * len(height)
    currentMax = 0
    for i, h in enumerate(reversed(height)):
        maxRight[len(height) - 1 - i] = currentMax
        if h > currentMax:
            currentMax = h

    maxWater = 0
    for i, h in enumerate(height):
        possibleWater = min(maxLeft[i], maxRight[i]) - h
        if possibleWater > 0:
            maxWater += possibleWater

    return maxWater


def trapWithNoExtraMemory(height):
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]

    maxTrap = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            maxTrap += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            maxTrap += rightMax - height[r]

    return maxTrap


print(trapWithExtraMemory([4,2,0,3,2,5]))
print(trapWithNoExtraMemory([4,2,0,3,2,5]))
