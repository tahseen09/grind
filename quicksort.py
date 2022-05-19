# ==============================================================================
# * Quicksort
# ! Time Complexity - O(n^2) - Worst Case, O(nlogn) - Average/Best Case
# ==============================================================================


def quicksort(nums: list) -> list:
    l = len(nums)
    if l < 2:
        return nums

    lesser = []
    greater = []
    pivot = nums[l // 2]
    for i, n in enumerate(nums):
        if i == l // 2:
            continue
        if n <= pivot:
            lesser.append(n)
        else:
            greater.append(n)
    res1 = quicksort(lesser)
    res2 = quicksort(greater)
    return res1 + [pivot] + res2


nums = [1, 2, 6, 5]
print(quicksort(nums))
