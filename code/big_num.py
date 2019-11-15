#data = list(map(int, input().split()))

data = [1, 2, 3, 4, 20]

res = [1, 2, 3, 4, 0]
num = data[-1]
if num == 1:
    print(1)
elif num == 2:
    print(2)
elif num == 3:
    print(3)
elif num == 4:
    print(4)
else:
    n = 4
    while n < 10000:
        res[n % 5] = res[ (n-1) % 5 ] + res[(n-3) % 5] + res[(n-4) % 5]
        n += 1

    i = (num - 1) % 5 
    ans = res[i] % (int(1e9 + 7))  # 1e9 + 7 是浮点数
    print(ans)
