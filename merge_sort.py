# ==============================================================================
# * Merge Sort
# ? Follows Divide & Conquer Idea
# ! Time Complexity
# ==============================================================================


def merge(res1, res2):
    # ? Merge two array in sorted fashion by comparing each indivual element. Each array is already sorted in itself.
    res = []
    p1, p2 = 0, 0
    l1, l2 = len(res1), len(res2)
    limit = min(l1, l2)

    while p1 < limit and p2 < l2:
        num1 = res1[p1]
        num2 = res2[p2]
        if num1 < num2:
            p1 += 1
            res.append(num1)
        else:
            p2 += 1
            res.append(num2)
    # ? Check for remaining elements
    if p1 < l1:
        res.extend(res1[p1:])
    elif p2 < l2:
        res.extend(res2[p2:])
    return res


def divide(nums):
    # ? Divide the nums array into two halves
    mid = len(nums) // 2
    return nums[:mid], nums[mid:]


def mergeSort(nums):
    if len(nums) == 1:
        return nums

    nums1, nums2 = divide(nums)
    res_1 = mergeSort(nums1)
    res_2 = mergeSort(nums2)
    return merge(res_1, res_2)


arr = [99, 98, 87, 1, 88, -1, 209]
print("result", mergeSort(arr))
