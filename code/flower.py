from functools import lru_cache

'''
连续的花
'''
#t, k = list(map(int, input().split()))
t, k = 3, 2

def solution(begin, end):

    @lru_cache(None)
    def dp(i):
        if 0 <= i < k:
            return 1
        return dp(i-1) + dp(i-k)

    sum_ = 0
    for i in range(begin, end+1):
        sum_ += dp(i)
    
    return sum_

print(solution(1, 100000))
     