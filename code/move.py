n, m = list(map(int,input().split()))
A = list(map(int, input().split()))
acc = sum(A)

def check(x):
    cnt, p = 0, 0
    for i in range(1, n+1):
        cnt += A[i-1]

        if i >= x:
            return False

        while i + cnt >= x:
            cnt -= x - i
            p += 1

            if p > m:
                return False

    if p == m:
        return cnt <= 0

    return True

if m > acc:
    print(n+1)
else:
    l, r = 2, n + acc
    while l < r:
        mid = l + r >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1

    print(r)


