def solution(total_disk,total_memory,app_list):
    
    # TODO Write your code here

    if total_disk < 0 or total_memory < 0:
        return -float("inf")

    if len(app_list) == 0:
        return 0
  
    len_ = len(app_list)   

    sol = max(app_list[0][2] + solution(total_disk - app_list[0][0], total_memory - app_list[0][1], app_list[1:]),
              solution(total_disk, total_memory, app_list[1:]))     
                
    return sol
            
def solution2(total_disk, total_memory, app_list):
    if total_disk < 0 or total_memory < 0:
        return 0

    if len(app_list) == 0:
        return 0

    def dp(i, v, u):
        if i == -1 or v < 0 or u < 0:
            return 0

        if v >= app_list[i][0] and u >= app_list[i][1]:
            return max(dp(i-1, v, u), dp(i-1, v-app_list[i][0], u-app_list[i][1])+ app_list[i][2])
        else:
            return dp(i-1, v, u)

    l = len(app_list)

    return dp(l-1, total_disk, total_memory)


def solution3(total_disk, total_memory, app_list):
    if total_disk < 0 or total_memory < 0:
        return 0

    if len(app_list) == 0:
        return 0

    dp = [[[0 for i in range(total_memory+1)] for j in range(total_disk + 1)] for k in range(len(app_list) + 1)]
    #dp = [[[0] * (total_memory + 1)] * (total_disk + 1)] * (len(app_list) + 1) * 值的引用, 对可变对像不安全

    for i in range(1, len(app_list)+1):
        for j in range(app_list[i-1][0], total_disk+1):
            for k in range(app_list[i-1][1], total_memory+1):
                dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-app_list[i-1][0]][k-app_list[i-1][1]] + app_list[i-1][2])

    return dp[len(app_list)][total_disk][total_memory]


if __name__ == "__main__":
    
    #input1 = input()
    #disk = int(input1.split()[0])
    #memory = int(input1.split()[1])
    #input2 = input1.split()[2]
    #app_list = [[int(j) for j in i.split(',')] for i in input2.split('#')]
    disk = 15
    memory = 10
    app_list = [[5, 1, 1000], [2, 3, 3000], [5, 2, 15000], [10, 4, 16000]]
    print(solution3(disk,memory,app_list))