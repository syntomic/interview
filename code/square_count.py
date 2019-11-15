import sys
lines = sys.stdin.readlines()
n = int(lines[0])
x1 = list(map(int,lines[1].split()))
y1 = list(map(int,lines[2].split()))
x2 = list(map(int,lines[3].split()))
y2 = list(map(int,lines[4].split()))
# 遍历所有点的组合（包含了矩形所有角以及交点），看一下有多少矩形包含它
res = 1
for x in x1+x2:
    for y in y1+y2:
        cnt = 0
        for i in range(n):
            if x > x1[i] and y > y1[i] and x <= x2[i] and y <= y2[i]:
                cnt += 1
        res = max(res,cnt)
print(res)