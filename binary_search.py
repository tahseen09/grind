# ==============================================================================
# * Binary Search
# ! Time Complexity - O(logN)
# ==============================================================================


def binary_search(nums: list, target: int) -> int:
    # TODO - search for an target in the list(nums), return the position
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def main():
    testcases = [
        ([1,2,3,4,5], 4),
        ([], 9),
        ([1], 0)
    ]
    for i, testcase in enumerate(testcases):
        try:
            expected_index = testcase[0].index(testcase[1])
        except ValueError:
            expected_index = -1
        index = binary_search(testcase[0], testcase[1])
        assert expected_index == index, f"Testcase {i+1} failed. {testcase[0]}, Expected - {expected_index}, Result - {index}"
        print(f"Testcase {i+1} passed")

main()
