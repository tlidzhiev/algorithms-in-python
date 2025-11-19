def find_kth_largest(nums, k):
    return quickselect(nums, 0, len(nums) - 1, k)


def quickselect(nums, left, right, k):
    if left == right:
        return nums[left]

    pivot_index = partition(nums, left, right)

    if k == pivot_index + 1:
        return nums[pivot_index]
    elif k < pivot_index + 1:
        return quickselect(nums, left, pivot_index - 1, k)
    else:
        return quickselect(nums, pivot_index + 1, right, k)


def partition(nums, left, right):
    pivot = nums[right]
    i = left

    for j in range(left, right):
        if nums[j] >= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[right] = nums[right], nums[i]
    return i
