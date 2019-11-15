from functools import lru_cache

def win_prob_of_A(numR, numB):
    
    @lru_cache(None)
    def dp(i,j):
        if i == 0:
            return -1
        if j == 0:
            return 1
        if j == 1 or i == 1:  ## 必须第一次拿到红球
            return i / (i + j)
        if j == 2:
            return i / (i + j) + i / (i + j) * (i - 1) / (i + j- 1)
        else:
            return (
                i / (i + j) + 
                j / (i + j) * (j - 1) / (i + j - 1) * (j - 2) / (i + j - 2) * dp(i, j - 3) + 
                j / (i + j) * (j - 1) / (i + j - 1) * i / (i + j - 2) * dp(i - 1, j - 2)
            )

    return dp(numR, numB)


if __name__ == "__main__":
    print(format(win_prob_of_A(3, 4), '.5f'))
                


