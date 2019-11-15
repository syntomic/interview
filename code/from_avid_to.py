#num = int(input())
num = 5
"""
最大链接数
"""
avid = {}
#dict_ = {}

'''for i in range(num):
    a, b = list(map(int, input().split()))
    if a not in avid:
        avid[a] = [b]
    else:
        avid[a].append(b)'''

avid = {33956:[27538, 84925], 79731:[91415, 25288], 25288:[33956]}

max_key = 0
max_cnt = 0

for k in avid.keys():
    list_ = avid[k]
    cnt = len(list_)
    
    while len(list_) != 0:
        list_in_key = []

        for i in list_:
            if i in avid.keys():
                list_in_key.extend(avid[i])

        cnt += len(list_in_key)
        
        list_ = list_in_key

    if max_cnt < cnt:
        max_cnt = cnt
        max_key = k
    elif max_cnt == cnt:
        if max_key < k:
            max_key = k 

#max_ = max(dict_, key=dict_.get)

print(max_key)