T = 10
for t_case in range(1, T + 1):
    L = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    for i in range(100):
        temp = 0
        for j in range(100):
            if table[j][i] == 1:
                temp = 1
            elif table[j][i] == 2:
                if temp == 1:
                    result += 1
                temp = 2

    print('#{} {}'.format(t_case, result))