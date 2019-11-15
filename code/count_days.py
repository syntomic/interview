

def count_range(num, k):
    res = 0
    if num % (k + 1) == 0:
        res += num // ( k + 1)
    else:
        res += num // ( k + 1) + 1

    return res

#num = int(input())
num = 1

A = []


for i in range(num):
    #a, b = list(map(int, input().split()))
    a, b = 1, 7
    must = b
    
    if b == 0:
        res = count_range(30, a)
    else:
        #B = list(map(int, input().split()))
        B = [5, 9, 13, 17, 21, 25, 29]
        C = []
        for i in B:
            C.append((i-a, i+a))

        res = 0

        if C[0][0] > 1:
            res = count_range(C[0][0] - 1, a)

        for j in range(0, len(C)- 1):
            if C[j][1] + 1 < C[j+1][0]:
                res += count_range(C[j+1][0] - C[j][1], a)

        if 30 - C[-1][1] > 1:
            res += count_range(30-C[-1][1], a)

    count =  must + res

    A.append(count)


for i in A:
    print(i)