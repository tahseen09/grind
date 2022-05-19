# ==============================================================================
# * Sum of numbers in an array using recursion
# ==============================================================================
def sum_of_numbers(nums: list, index: int = 0, s: int = 0) -> int:
    l = len(nums)
    if index < l:
        s += nums[index]
        return sum_of_numbers(nums, index + 1, s)
    return s


s = sum_of_numbers([1, 2, 3])
print(s)
