from functools import lru_cache

def largest_common_substring(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0

    @lru_cache(None)
    def dp(i, j):
        if i == -1 or j == -1:
            return 0
        if s1[i] == s2[j]:
            return dp(i-1, j-1) + 1
        else:
            return 0

    max_ = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            max_ = max(dp(i, j), max_)  ## 需要改进, 重复计算

    return max_

def LCS(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0

    @lru_cache(None)
    def dp(i, j):
        if i == -1 or j == -1:
            return 0

        if s1[i] == s2[j]:
            return dp(i - 1, j - 1) + 1
        else:
            return max(dp(i, j - 1), dp(i - 1, j))
    
    max_ = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            max_ = max(dp(i, j), max_)

    return max_

if __name__ == "__main__":
    s1 = 'abgde'
    s2 = 'abcde'
    print(largest_common_substring(s1, s2))
    print(LCS(s1, s2))