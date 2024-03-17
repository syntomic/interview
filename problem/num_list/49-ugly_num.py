def is_ugly(num):
    """判断num是否为丑数"""
    while num % 2 == 0:
        num /= 2

    while num % 3 == 0:
        num /= 3

    while num % 5 == 0:
        num /= 5

    return num == 1

def get_ugly_num_1(index):
    """逐个得到第index个丑数"""
    if index <= 0:
        return 0

    num = 0
    ugly_found = 0

    while ugly_found < index:

        num += 1

        if is_ugly(num):

            ugly_found += 1

    return num

def get_ugly_num_2(index):
    """空间换时间"""
    if index <= 0:
        return 0

    ugly_nums = [0]*index
    ugly_nums[0] = 1
    next_ugly_index = 1

    multiply_2_index = 0
    multiply_3_index = 0
    multiply_5_index = 0

    while next_ugly_index < index:

        min_ = min(ugly_nums[multiply_2_index] * 2, ugly_nums[multiply_3_index] * 3, ugly_nums[multiply_5_index] * 5)
        ugly_nums[next_ugly_index] = min_

        while ugly_nums[multiply_2_index] * 2 <= min_:
            multiply_2_index += 1

        while ugly_nums[multiply_3_index] * 3 <= min_:
            multiply_3_index += 1

        while ugly_nums[multiply_5_index] * 5 <= min_:
            multiply_5_index += 1

        next_ugly_index += 1

    return ugly_nums[-1]

if __name__ == "__main__":
    print(get_ugly_num_1(500))
    print(get_ugly_num_2(500))