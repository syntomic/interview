# 整数数列A = [A_1, ..., A_n], B_i = max(0, A_{i+1} - A_i), 求A排列A'使得sum(B_i)最大

def max_sum_B(A):
    n = len(A)
    A_sorted = sorted(A)
    A_prime = [0] * n
    i, j = 0, n-1
    for k in range(n):
        if k % 2 == 1:
            A_prime[k] = A_sorted[j]
            j -= 1
        else:
            A_prime[k] = A_sorted[i]
            i += 1
    B = [max(0, A_prime[i+1]-A_prime[i]) for i in range(n-1)]
    max_B_sum = sum(B)
    return max_B_sum, A_prime

if __name__ == "__main__":
    print(max_sum_B([1, 2, 3, 4]))



