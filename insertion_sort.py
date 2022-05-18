# Implement Insertion Sort

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

nums = [2,9,0,1,8,7,0,2,4,78,98,76,-1,-5]
print(insertion_sort(nums))