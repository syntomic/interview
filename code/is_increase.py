def find_root_in_data(data, num_of_node):
    list_ = list(range(num_of_node))
    for i in data:
        for j in i:
            if j != -1:
                list_[j] = -1
    
    return sorted(list_)[-1]
     


#num_of_example = int(input())
num_of_example = 1
answer = []

for i in range(num_of_example):
    #num_of_node = int(input())
    num_of_node = 8

    '''data = []
    for j in range(num_of_node):
        data.append(map(int, input().split()))'''

    data = [[2, -1, -1], [1, 5, 3], [4, -1, 6], [2, -1, -1], [3, 0, 2], [2, 4, 7], [7, -1, -1], [2, -1, -1]]
    root = find_root_in_data(data, num_of_node)
    nodes = [root]

    for j in range(num_of_node):
        current_sum = sum([data[i][0] for i in nodes])

        next_nodes = []
        for i in nodes:
            for j in data[i][1:]:
                if j != -1:
                    next_nodes.append(j)

        next_sum = sum([data[i][0] for i in next_nodes])

        if next_sum == 0:
            answer.append('yes')
            break

        if next_sum <= current_sum:
            answer.append('no')
            break
        
        nodes = next_nodes

for k in answer:
    print(k)

