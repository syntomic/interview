from functools import lru_cache


def solution(nums):

    @lru_cache(None)
    def dp(i, inc=True):
        if i == 0:
            return 1

        res = 1

        for j in range(i):
            if inc:
                if nums[j] < nums[i]:
                    res = max(res, dp(j) + 1)
            else:
                if nums[j] > nums[i]:
                    res = max(res, dp(j, inc=False) + 1)

        return res
        
    max_ = max(dp(len(nums)-1), dp(len(nums)-1, inc=False))

    return len(nums) - max_


print(solution([8, 2, 7, 6]))