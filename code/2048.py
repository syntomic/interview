"""2048游戏消除"""

def merge_same_forward(nums):
    l = len(nums)
    res = []
    j = 0
    while j < len(nums):
        res.append(nums[j])
        if j == l - 1:
            break
        else:
            if res[-1] != nums[j+1]:
                j += 1
            else:
                res[-1] = res[-1] * 2
                j += 2

    return res

def one_line(line):

    line_without_zero = list(filter(lambda x : x != 0, line))

    
    forward = merge_same_forward(line_without_zero)
    backward = merge_same_forward(forward[::-1])[::-1]
    backward.extend([0]*(len(line) - len(backward)))

    return backward
    	
print(one_line([8,4,0,4]))