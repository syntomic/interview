import time

def removeBoxes(A):
    N = len(A)
    memo = [[[0]*N for _ in range(N) ] for _ in range(N) ]
    
    def dp(i, j, k):
        if i > j: return 0
        if not memo[i][j][k]:
            m = i
            while m+1 <= j and A[m+1] == A[i]:
                m += 1
            i, k = m, k + m - i
            ans = dp(i+1, j, 0) + (k+1) ** 2
            for m in range(i+1, j+1):
                if A[i] == A[m]:
                    ans = max(ans, dp(i+1, m-1, 0) + dp(m, j, k+1))
            memo[i][j][k] = ans
        return memo[i][j][k]
    
    return dp(0, N-1, 0)

start = time.time()
print(removeBoxes([1, 4, 1, 3, 3, 3, 2, 4, 1]))
print(time.time()-start)


nums = [1, 4, 2, 2, 3, 3, 2, 4, 1]
def solution(nums):
    if len(nums) == 0:
        return 0

    A = []
    i = 0
    while i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            begin = i
            end = i + 1
            while end < len(nums) - 1 and nums[end+1] == nums[i]:
                end += 1
            i = end + 1
            A.append((begin, end))
        else:
            i += 1
        

    if len(A) == 0:
        return 0

    res = 0
    for a in A:
        sum_ = (a[1]-a[0] + 1) ** 2 + solution(nums[:a[0]] + nums[a[1]+1:])
        res = max(res, sum_)

    return res
        
start = time.time()
print(solution([1, 4, 1, 3, 3, 3, 2, 4, 1]))
print(time.time()-start)