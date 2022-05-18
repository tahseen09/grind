# ==============================================================================
# * Insertion Sort
# ! Time Complexity - O(N^2)
# ==============================================================================

def insertion_sort(nums: list) -> list:
    l = len(nums)
    for i in range(1, l):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = key
    return nums

def main():
    testcases = [[], [2, 1], [99, 98, 10000000, 1, 88, -1, 209]]
    for i, testcase in enumerate(testcases):
        expected = sorted(testcase)
        result = insertion_sort(testcase)
        assert expected == result, f"Testcase {i+1} failed"
        print(f"Testcase {i+1} passed")

main()