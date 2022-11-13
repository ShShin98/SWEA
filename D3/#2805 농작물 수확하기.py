T = int(input())

for t_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    result = 0
    start = N // 2
    end = start + 1

    for i in range(N):
        result += sum(farm[i][start:end])

        if i < N // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    
    print('#{} {}'.format(t_case, result))