import sys 
for line in sys.stdin:
    a = line.split()  
    a = a[0]
    a = a.split(',')
    a = list(map(int, a))
    print(a)


    res, step = 0, 0
    for i in a:
        res += max(step, i) - i
        step = max(step, i) + 1
        
    print(res)