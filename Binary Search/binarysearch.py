def binarySearch(s, target):

    lo, hi = 0, len(s)-1
    floor = ceil = -1

    while lo <= hi:

        mid = (lo + hi) // 2
        if s[mid] == target:
            return mid, mid
        elif s[mid] < target:
            floor = mid
            lo = mid + 1
        else:
            ceil = mid
            hi = mid - 1

    return floor, ceil

s = [1,3]
target = 0

print(binarySearch(s, target))