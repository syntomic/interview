from collections import deque

stack = deque()

def solution(s):

    # Write your code here

    l = len(s)
    
    stack.append(s[0])

    i = 1
    while i < l and stack[-1] != '0':
        if s[i] == ')':
            stack.pop()
        else:
            stack.append(s[i])
        
        i += 1

    return len(stack) - 1

if __name__ == '__main__':
    input = '((0))'
    print(solution(input))