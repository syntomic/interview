'''
Leetcode 903
'''
from functools import lru_cache

class Solution:
    def numPermsDISequence(self, S):
        MOD = 10**9 + 7
        N = len(S)

        @lru_cache(None)
        def dp(i, j):
            ## {0, 1, ..., i} 中长度为i+1, 并以数字j作为最后一个数字的排列的数量
            if not(0 <= j <= i):
                return 0
            if i == 0:
                return 1
            elif S[i-1] == 'D':
                return (dp(i, j+1) + dp(i-1, j)) % MOD  ## sum(dp(i-1, k) for k in range(j, i)) % MOD
                                                         ## 1 5 2 0 4 3 <- 1 4 2 0 3
            else:
                return (dp(i, j-1) + dp(i-1, j-1)) % MOD ## sum(dp(i-1, k) for k in range(j)) % MOD

        return sum(dp(N, j) for j in range(N+1)) % MOD


class Solution2:
    def numPermsDISequence(self, S):
        MOD = 10**9 + 7

        fac = [1, 1]
        for x in range(2, 201):
            fac.append(fac[-1] * x % MOD)
        facinv = [pow(f, MOD-2, MOD) for f in fac]

        def binom(n, k):
            return fac[n] * facinv[n-k] % MOD * facinv[k] % MOD

        @lru_cache(None)
        def dp(i, j):
            if i >= j: return 1
            ans = 0
            n = j - i + 2
            if S[i] == 'I': ans += dp(i+1, j)
            if S[j] == 'D': ans += dp(i, j-1)

            for k in range(i+1, j+1):
                if S[k-1:k+1] == 'DI':
                    ans += binom(n-1, k-i) * dp(i, k-2) % MOD * dp(k+1, j) % MOD
                    ans %= MOD
            return ans

        return dp(0, len(S) - 1)

'''Leetcode 903'''

class Solution3():
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [1] * (len(S) + 1)
        for c in S:
            if c == "I":
                dp = dp[:-1]
                for i in range(1, len(dp)):
                    dp[i] += dp[i - 1]
            else:
                dp = dp[1:]
                for i in range(len(dp) - 1)[::-1]:
                    dp[i] += dp[i + 1]
        return dp[0] % (10**9 + 7)
if __name__ == "__main__":
    sol = Solution()
    print(sol.numPermsDISequence("DID"))