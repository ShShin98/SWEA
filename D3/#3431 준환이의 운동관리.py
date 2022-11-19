T = int(input())
for t_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    result = -1
    if X < L:
        result = L-X
    elif L <= X <= U:
        result = 0
    print('#{} {}'.format(t_case, result))