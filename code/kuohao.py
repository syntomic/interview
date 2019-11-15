def isValid(str):
    # 判断该字符串是否是合法的括号序列
    stack = []
    for i in range(len(str)):
        if str[i] == '(':
            stack.append(str[i])
        else:
            # 去stack里匹配一个左括号
            if len(stack) == 0 or stack[-1] != '(':
                return False
            else:
                stack.pop()
 
    return not stack
 
# 得到输入字符串
input_str = input()
n = len(input_str)
# 思路：取出字符串中的某一个字符c，得到一个剩余字符串remain_str，依次把c插入到remain_str中
# 得到新的字符串，如果该字符串是合法的括号序列，并且与源字符串不相等，则个数加1
# 关键点：对于LCS(s, t)，必然会存在长度为len(s) - 1的公共子序列
count = 0
new_str_list = []
for i in range(n):
    c = input_str[i]
    remain_str = input_str[:i] + input_str[i + 1:]
    # 分别把c插入到remain_str中
    for j in range(len(remain_str) + 1):
        new_str = remain_str[:j] + c + remain_str[j:]
        # 判断new_str是否是合法的括号序列，并且与源字符串不相等，并且这个new_str也不能重复
        if new_str != input_str and isValid(new_str) and new_str not in new_str_list:
            new_str_list.append(new_str)
            count += 1
 
print(count)
