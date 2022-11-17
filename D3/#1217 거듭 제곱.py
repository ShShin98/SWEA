def func(n, m):
    if m == 1:
        return n

    return n * func(n, m - 1)

T = 10
for t_case in range(1, T + 1):
    t = int(input())
    n, m = map(int, input().split())
    result = func(n, m)
    print('#{} {}'.format(t_case, result))