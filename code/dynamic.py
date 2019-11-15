def get_climbing_ways(n):
    """递归解法, 时间复杂度O(2^n)"""
    if n < 1:
        return 0

    if n == 1:
        return 1
    
    if n == 2:
        return 2

    return get_climbing_ways(n-1) + get_climbing_ways(n-2)

def get_climbing_ways2(n):
    """备忘录算法, 时间和空间复杂度为O(n)"""
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    dict_ = {}
    if n in dict_:
        return dict_[n]
    else:
        value = get_climbing_ways2(n-1) + get_climbing_ways2(n-2)
        dict_[n] = value
        return value


def get_climbing_ways3(n):
    """动态规划, 时间复杂度O(n), 空间复杂度O(1)"""
    if n < 1:
        return 0

    if n == 1:
        return 1
    
    if n == 2:
        return 2

    a = 1
    b = 2
    temp = 0

    for i in range(3, n+1):
        temp = a + b
        a = b
        b = temp

    return temp