n = int(input())

dif = []

for _ in range(n):
    data = list(map(int, input().split()))
    dif.append([data[0] - data[1], data[0], data[1]])

dif.sort(key=lambda x: -x[0])

res = 0
for k, v in enumerate(dif):
    res += (k + 1)*v[0] + v[2]*n - v[1]

print(res)