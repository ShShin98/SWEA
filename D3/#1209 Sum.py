T = 10
for t_case in range(1, T + 1):
    t_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    diag1 = 0
    diag2 = 0

    for i in range(100):
        result = max(result, sum(arr[i]))
        temp = 0

        for j in range(100):
            temp += arr[j][i]
            if i == j:
                diag1 += arr[j][i]
            if i + j == 99:
                diag2 += arr[j][i]

        result = max(result, temp)
        
    result = max(result, diag1, diag2)

    print('#{} {}'.format(t_case, result))