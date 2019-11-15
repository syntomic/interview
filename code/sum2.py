def solution1(data):
    n = len(data)
    res = 0
    for i, v in enumerate(data):
        min_ = v
        sum_ = v
        j = i
        while i > 0:
            if v <= data[i-1]:
                sum_ += data[i-1]
                i -= 1
            else:
                break
        i = j
        while i < n - 1:
            if v <= data[i+1]:
                sum_ += data[i+1]
                i += 1
            else:
                break
    
        res = max(res, min_*sum_)

    return res


def solution2(data):
    data.append(0)
    res = 0
    s = []
    pre = [0]*len(data) # 前缀和

    for i in range(1, len(data)):
        pre[i] += pre[i-1] + data[i-1]

    for i, v in enumerate(data):
        while s and v <= data[s[-1]]:
            t = s.pop()
            res = max(res, data[t]*(pre[i] - pre[s[-1] + 1 if s else 0]))

        s.append(i)

    return res


if __name__ == "__main__":
    data = [7, 2, 4, 6, 5]
    data1 = [6, 2, 4, 7, 5]
    print(solution1(data1))
    print(solution2(data1))