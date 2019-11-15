def del_duplicate_after_square(nums):
    if nums == []:
        return 0

    if len(nums) == 1:
        return 1

    l = len(nums)
    p = 0
    q = l - 1
    ans = 0

    while p <= q:
        if abs(nums[p]) > abs(nums[q]):
            ans += 1
            p += 1
        elif abs(nums[p]) == abs(nums[q]):
            ans += 1
            temp = nums[q]
            p += 1
            q -= 1
            if p < l and temp == abs(nums[p]):
                p += 1
            if q > -1 and temp == abs(nums[q]):
                q -= 1
        else:
            ans += 1
            q -= 1
    
    return ans

            

if __name__ == "__main__":
    nums = [-5, -3, -1, 0, 1, 1, 3, 3]
    nums1 = [-2, 1, 1]
    print(del_duplicate_after_square(nums1))