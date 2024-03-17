# 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def min_sub_array_len(nums, target):
    left, right = 0, 0
    n = len(nums)
    _sum = 0
    ans = float('inf')
    while right < n:
        _sum += nums[right]
        while _sum >= target:
            if _sum == target:
                ans = min(ans, right - left + 1)
            _sum -= nums[left]
            left += 1
        right += 1
    return ans if ans != float('inf') else 0

assert min_sub_array_len([2,3,1,2,4,3], 7) == 2
assert min_sub_array_len([1,4,4],4) == 1
assert min_sub_array_len([1,1,1,1,1,1,1,1], 11) == 0

print(min_sub_array_len([2,3,8], 7))