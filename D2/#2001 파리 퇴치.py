T = int(input())

for test_case in range (1, T + 1):
    n, m = map(int, input().split())
    flyArr = []
    result = 0

    for _ in range(n):
        flyArr.append(list(map(int, input().split())))

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            cnt = 0
            for x in range(m):
                for y in range(m):
                    cnt += flyArr[i + x][j + y]
            result = max(result, cnt)

    print('#{} {}'.format(test_case, result))