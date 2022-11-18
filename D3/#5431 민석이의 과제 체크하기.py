T = int(input())
for t_case in range(1, T + 1):
    N, K = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    result = []

    for i in range(1, N + 1):
        if i not in nums:
            result.append(i)

    print('#{} {}'.format(t_case, ' '.join(map(str, result))))