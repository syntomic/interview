class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # dp[i, j]代表i到j位置是否是回文字符串
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = ""
        max_len = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # dp[i][j] == dp[i+1][j-1] && s[i] == b  s[j]
                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])
                if dp[i][j] and j - i + 1 > max_len:
                    ans = s[i:j + 1]
                    max_len = j - i + 1
        return ans

if __name__ == "__main__":
    sol = Solution()

    print(sol.longestPalindrome("adbbdads"))