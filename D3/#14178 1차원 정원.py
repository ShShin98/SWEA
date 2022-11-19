T = int(input())
for t_case in range(1, T + 1):
    N, D = map(int, input().split())
    result = N // (D * 2 + 1) if N % (D * 2 + 1) == 0 else N // (D * 2 + 1) + 1
    print('#{} {}'.format(t_case, result))